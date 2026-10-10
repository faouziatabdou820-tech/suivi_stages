from django.db import models
from .etudiant import Etudiant
from .offre import Offre

class Candidature (models.Model): 
    status = models.BooleanField()
    date_depot = models.DateField()

    
    class Statut(models.TextChoices):
        DEPOSEE = "deposee", "Déposée"
        RETENUE = "retenue", "Retenue"
        REFUSEE = "refusee", "Refusée"

    etudiant = models.ForeignKey(Etudiant,on_delete=models.PROTECT, related_name="candidatures")
        

    offre = models.ForeignKey(
        Offre,
        on_delete=models.PROTECT,
        related_name="candidatures"
    )


    date_depot = models.DateField()
    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.DEPOSEE
    )


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["etudiant", "offre"],
                name="une_candidature_par_etudiant_et_offre"
            )
        ]



    def __str__(self):
        return f"{self.etudiant} - {self.offre}"
