from django.shortcuts import get_object_or_404, render
from stages.models import Entreprise


# Create your views here.
def liste_entreprises(request):
        return render(
        request,
        "stages/entreprise_liste.html",
        {"entreprises": Entreprise.objects.all()}
)


def entreprise_detail(request,pk) : 
        entreprise = get_object_or_404(Entreprise,pk = pk)
        offres = entreprise.offres.all()
        return render(request,"stages/entreprise_detail.html",{"entreprise" : entreprise, "offres" : offres})