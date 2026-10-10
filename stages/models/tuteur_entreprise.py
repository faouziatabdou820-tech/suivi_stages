from django.db import models
from .personne import Personne

from .entreprise import Entreprise
from .etudiant import Etudiant


class TuteurEntreprise(Personne) : 

     #etudiant = models.ForeignKey(Etudiant,on_delete=models.SET_NULL,related_name="tuteurs")
    entreprise = models.ForeignKey(Entreprise,on_delete=models.PROTECT,related_name="tuteurs")




def __str__(self):
        return f"{self.prenom} {self.nom}"