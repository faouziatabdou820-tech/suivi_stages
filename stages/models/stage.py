from django.db import models
from .candidature import Candidature
from .tuteur_entreprise import TuteurEntreprise
from .enseignant_referent import EnseignantReferent


class Stage(models.Model):
    candidature = models.OneToOneField(
        Candidature,
        on_delete=models.PROTECT,
        related_name="stage"
    )

    tuteur = models.ForeignKey(
        TuteurEntreprise,
        on_delete=models.PROTECT,
        related_name="stages"
    )

    enseignant_referent = models.ForeignKey(
        EnseignantReferent,
        on_delete=models.PROTECT,
        related_name="stages"
    )

    sujet = models.CharField(max_length=255)

    def __str__(self):
        return self.sujet