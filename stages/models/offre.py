from django.db import models

from .competence import Competence
from .entreprise import Entreprise


class Offre(models.Model):
    titre = models.CharField(max_length=120)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.PositiveIntegerField()
    description = models.TextField()



    entreprise = models.ForeignKey(Entreprise ,on_delete = models.PROTECT,related_name="offres")
    competence = models.ManyToManyField(Competence, related_name= "offres")


   