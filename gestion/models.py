from django.db import models
from django.utils import timezone


class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    fichier = models.FileField(
        upload_to="cours_fichiers/", blank=True, null=True
    )  # Pour uploader un fichier
    date_creation = models.DateTimeField(default=timezone.now)
    date_modification = models.DateTimeField(auto_now=True)
    genere_par_ia = models.BooleanField(default=False)

    def __str__(self):
        return self.titre
