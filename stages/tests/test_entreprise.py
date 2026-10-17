from stages.models import Entreprise



def test_une_entreprise_s_affiche_avec_sa_ville(db):

    entreprise = Entreprise.objects.create(
        nom = "sokode numerique",
        ville = "sokode",
        secteur = "service informatiques",
     )


    assert str(entreprise)  == "sokode numerique (sokode)"