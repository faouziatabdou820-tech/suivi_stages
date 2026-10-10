from django.urls import path
from . import views


app_name = "stages"

urlpatterns = [
    path("", views.offre_liste,name = "offre_liste"),
    path("offres/<int:pk>/", views.offre_detail, name = "offre_detail"),
    path("entreprises/", views.liste_entreprises,name ="entreprise_liste"),
    path("entreprises/<int:pk>/", views.entreprise_detail, name = "entreprise_detail"),

]