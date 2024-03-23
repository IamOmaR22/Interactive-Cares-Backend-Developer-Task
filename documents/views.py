from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Document
from users.models import CustomUser
from .serializers import DocumentSerializer, DocumentCreateSerializer, DocumentUpdateSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def document_list_create(request):
    if request.method == 'GET':
        documents = Document.objects.filter(owner=request.user)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DocumentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk, owner=request.user)
    except Document.DoesNotExist:
        return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DocumentUpdateSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        document.delete()
        return Response({'message': 'Document deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_update_access(request, pk):
    try:
        document = Document.objects.get(pk=pk, owner=request.user)
    except Document.DoesNotExist:
        return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)

    shared_with = request.data.get('shared_with', [])
    document.shared_with.clear()
    for user_id in shared_with:
        user = CustomUser.objects.filter(pk=user_id).first()
        if user:
            document.shared_with.add(user)

    return Response({'message': 'Access updated successfully'}, status=status.HTTP_200_OK)
