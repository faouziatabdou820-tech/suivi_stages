from django.db import models
from django.shortcuts import render
# Create your models here.
class Entreprise(models.Model):

    nom = models.CharField(max_length=120)
    secteur = models.CharField(max_length=150)
    ville = models.CharField(max_length=80)
    email = models.EmailField()

    class Meta:
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
            fields = ["nom","ville"],
            name = "unique_entreprise_par_ville",
            )
        ]


    def __str__(self):
        return f"{self.nom}({self.ville})"



   
