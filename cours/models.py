from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    fichier = models.FileField(upload_to='cours_fichiers/', blank=True, null=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
