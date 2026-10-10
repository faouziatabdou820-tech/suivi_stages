# 
from datetime import date

from stages.models import (
    Candidature, Competence, EnseignantReferent, Entreprise,
    Etudiant, Offre, Stage, TuteurEntreprise,
)

# ---------- Compétences ----------
print("\n--- COMPETENCES ---")
django, _ = Competence.objects.get_or_create(libelle="Django")
python, _ = Competence.objects.get_or_create(libelle="Python")
sql, _ = Competence.objects.get_or_create(libelle="SQL")
html, _ = Competence.objects.get_or_create(libelle="HTML")
javascript, _ = Competence.objects.get_or_create(libelle="JavaScript")
print("Compétences :", list(Competence.objects.all()))

# ---------- Entreprises (deux à Sokodé) ----------
print("\n--- ENTREPRISES ---")
entreprise1, _ = Entreprise.objects.get_or_create(
    nom="TogoTech", defaults={"secteur": "Informatique", "ville": "Sokodé"})
entreprise2, _ = Entreprise.objects.get_or_create(
    nom="AgroPlus", defaults={"secteur": "Agriculture", "ville": "Sokodé"})
entreprise3, _ = Entreprise.objects.get_or_create(
    nom="LoméSoft", defaults={"secteur": "Informatique", "ville": "Lomé"})
print("Entreprises :", list(Entreprise.objects.all()))

# ---------- Tuteurs ----------
print("\n--- TUTEURS ---")
tuteur1, _ = TuteurEntreprise.objects.get_or_create(
    email="tuteur1@example.com",
    defaults={"nom": "Mensah", "prenom": "Koffi", "sexe": "M",
              "date_naissance": date(1985, 4, 12), "entreprise": entreprise1},
)
tuteur2, _ = TuteurEntreprise.objects.get_or_create(
    email="tuteur2@example.com",
    defaults={"nom": "Assogba", "prenom": "Afi", "sexe": "F",
              "date_naissance": date(1988, 9, 20), "entreprise": entreprise2},
)
print("Tuteurs :", list(TuteurEntreprise.objects.all()))

# ---------- Enseignants référents ----------
print("\n--- ENSEIGNANTS REFERENTS ---")
enseignant1, _ = EnseignantReferent.objects.get_or_create(
    email="enseignant1@example.com",
    defaults={"nom": "Doe", "prenom": "Jean", "sexe": "M",
              "date_naissance": date(1978, 2, 10)},
)
enseignant2, _ = EnseignantReferent.objects.get_or_create(
    email="enseignant2@example.com",
    defaults={"nom": "Kossi", "prenom": "Marie", "sexe": "F",
              "date_naissance": date(1982, 6, 15)},
)
print("Enseignants :", list(EnseignantReferent.objects.all()))

# ---------- Étudiants ----------
print("\n--- ETUDIANTS ---")
etudiants_data = [
    (1001, "Koffi", "Ama", "F", date(2002, 5, 10), "ama.koffi@example.com"),
    (1002, "Mensah", "Kossi", "M", date(2001, 8, 15), "kossi.mensah@example.com"),
    (1003, "Assogba", "Afi", "F", date(2002, 3, 20), "afi.assogba@example.com"),
    (1004, "Tchalla", "Kodjo", "M", date(2001, 11, 2), "kodjo.tchalla@example.com"),
    (1005, "Akakpo", "Mawuli", "M", date(2002, 7, 12), "mawuli.akakpo@example.com"),
]
etudiants = []
for matricule, nom, prenom, sexe, naissance, email in etudiants_data:
    e, _ = Etudiant.objects.get_or_create(
        matricule=matricule,
        defaults={"nom": nom, "prenom": prenom, "sexe": sexe,
                  "date_naissance": naissance, "email": email,
                  "promotion": 2025},
    )
    etudiants.append(e)
etudiant1, etudiant2, etudiant3, etudiant4, etudiant5 = etudiants

etudiant1.competences.set([django, python, sql])
etudiant2.competences.set([python, javascript])
etudiant3.competences.set([django, html])
etudiant4.competences.set([sql, python])
etudiant5.competences.set([django, javascript, html])
print("Etudiants :", list(Etudiant.objects.all()))

# ---------- Offres ----------
print("\n--- OFFRES ---")
offre1, _ = Offre.objects.get_or_create(
    titre="Développeur Django", entreprise=entreprise1,
    defaults={"description": "Développement d'une application web avec Django.",
              "date_debut": date(2026, 6, 1), "date_fin": date(2026, 9, 30),
              "nb_places": 2},
)
offre2, _ = Offre.objects.get_or_create(
    titre="Développeur Python", entreprise=entreprise2,
    defaults={"description": "Développement d'une application Python.",
              "date_debut": date(2026, 6, 15), "date_fin": date(2026, 10, 15),
              "nb_places": 1},
)
offre3, _ = Offre.objects.get_or_create(
    titre="Développeur Web", entreprise=entreprise3,
    defaults={"description": "Création d'une plateforme web.",
              "date_debut": date(2026, 7, 1), "date_fin": date(2026, 10, 31),
              "nb_places": 2},
)

# Champ au singulier, comme dans votre modèle actuel.
# Si vous l'avez renommé en "competences", ajoutez le "s" ici.
offre1.competence.set([django, python])
offre2.competence.set([python, sql, javascript])
offre3.competence.set([django, html, javascript])
print("Offres :", list(Offre.objects.all()))

# ---------- Candidatures (6, statuts variés) ----------
print("\n--- CANDIDATURES ---")
# Si votre modèle a aussi un champ "status", il est rempli automatiquement.
champs_candidature = {f.name for f in Candidature._meta.get_fields()}


def candidater(etudiant, offre, jour, statut):
    defaults = {"date_depot": jour, "statut": statut}
    if "status" in champs_candidature:
        defaults["status"] = (statut == "RETENUE")
    obj, _ = Candidature.objects.get_or_create(
        etudiant=etudiant, offre=offre, defaults=defaults)
    return obj


candidature1 = candidater(etudiant1, offre1, date(2026, 2, 1), "RETENUE")
candidature2 = candidater(etudiant2, offre1, date(2026, 2, 3), "REFUSEE")
candidature3 = candidater(etudiant3, offre2, date(2026, 2, 5), "RETENUE")
candidature4 = candidater(etudiant4, offre2, date(2026, 2, 7), "DEPOSEE")
candidature5 = candidater(etudiant5, offre3, date(2026, 2, 10), "DEPOSEE")
candidature6 = candidater(etudiant1, offre3, date(2026, 2, 12), "REFUSEE")
print("Nombre de candidatures :", Candidature.objects.count())

# ---------- Stages (issus de candidatures retenues) ----------
print("\n--- STAGES ---")
stage1, _ = Stage.objects.get_or_create(
    candidature=candidature1,
    defaults={"tuteur": tuteur1, "enseignant_referent": enseignant1,
              "sujet": "Développement d'une application web avec Django"},
)
stage2, _ = Stage.objects.get_or_create(
    candidature=candidature3,
    defaults={"tuteur": tuteur2, "enseignant_referent": enseignant2,
              "sujet": "Développement d'une plateforme de gestion"},
)
print("Stages :", list(Stage.objects.all()))

# ---------- Les six requêtes du TP ----------
print("\n================ REQUETES DU TP ================")

print("\n1. Offres des entreprises de Sokodé :")
print(list(Offre.objects.filter(entreprise__ville="Sokodé")))

print("\n2. Etudiants ayant la compétence Django :")
print(list(Etudiant.objects.filter(competences__libelle="Django")))

print("\n3. Candidatures de l'étudiant 1 :")
print(list(Candidature.objects.filter(etudiant=etudiant1)))

print("\n4. Nombre de candidatures retenues :")
print(Candidature.objects.filter(statut="RETENUE").count())

print("\n5. Stages dont l'offre vient d'une entreprise de Sokodé :")
print(list(Stage.objects.filter(
    candidature__offre__entreprise__ville="Sokodé")))

print("\n6. Offres demandant une compétence de l'étudiant 1 :")
sans_distinct = Offre.objects.filter(
    competence__in=etudiant1.competences.all())
print("Sans distinct :", sans_distinct.count(), "résultats")
avec_distinct = sans_distinct.distinct()
print("Avec distinct :", avec_distinct.count(), "résultats")
print("Offres qui existent vraiment :", Offre.objects.count())