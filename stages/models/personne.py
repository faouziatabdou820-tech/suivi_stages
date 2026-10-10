from django.db import models


class Personne(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    sexe = models.CharField()
    date_naissance = models.DateField()
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ["nom"]  # noqa: RUF012
