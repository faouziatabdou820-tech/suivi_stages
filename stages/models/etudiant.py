from django.db import models

from .personne import Personne
from .competence import Competence

class Etudiant(Personne):
    matricule = models.IntegerField()
    promotion = models.CharField()

    competences = models.ManyToManyField(
        Competence,
        related_name="etudiants"
    )


    def __str__(self):
        return f"{self.prenom} {self.nom}"