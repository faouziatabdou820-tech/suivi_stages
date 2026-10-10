from django.contrib import admin

from stages.models import (
    Entreprise,
    Personne,
    Etudiant,
    TuteurEntreprise,
    EnseignantReferent,
    Competence,
    Offre,
    Candidature,
    Stage,
)


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ("nom", "ville")

@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'entreprise')


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("matricule", "nom", "prenom")


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ("titre", "entreprise", "date_debut")


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ("etudiant", "offre", "statut")


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ("sujet", "tuteur", "enseignant_referent")



@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')



@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('libelle',)