from django.shortcuts import get_object_or_404, render
from stages.models import Offre




def _offres() :
    return Offre.objects.select_related("entreprise").prefetch_related("competence")


def offre_liste(request) :
    return render(request,"stages/offre_liste.html",{"offres":_offres()})


def offre_detail(request,pk) : 
    offre = get_object_or_404(_offres(),pk = pk)
    return render(request,"stages/offre_detail.html",{"offre" : offre})