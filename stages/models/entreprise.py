from django.db import models


# from django.shortcuts import render
# Create your models here.
class Entreprise(models.Model):

    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=255)
    secteur = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)

   

    class Meta:
        ordering = ["nom"]
        constraints = [
            models.UniqueConstraint(
            fields = ["nom","ville"],
            name = "unique_entreprise_par_ville",
            )
        ]



    def __str__(self):

        return f"{self.nom} ({ self.ville})"
