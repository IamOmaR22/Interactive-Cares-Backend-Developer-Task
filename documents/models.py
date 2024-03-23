from django.db import models
from users.models import CustomUser

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_documents')
    shared_with = models.ManyToManyField(CustomUser, related_name='shared_documents', blank=True)

    def __str__(self):
        return self.title
