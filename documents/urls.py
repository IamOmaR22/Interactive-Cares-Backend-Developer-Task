from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list_create, name='document_list_create'),
    path('documents/<int:pk>/', views.document_detail, name='document_detail'),
    path('documents/<int:pk>/access/', views.add_update_access, name='add_update_access'),
]
