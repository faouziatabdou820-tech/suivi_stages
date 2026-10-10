Nombre d'offres : 3
sans rien : 7
avec select_related : 4
avec les deux : 2

# Explication
d - `select_related("entreprise")` a supprimé les 3 requêtes sur l'entreprise : elle est chargée dans la même requête que l'offre, grâce à un JOIN (7 → 4).

e - `prefetch_related("competence")` a supprimé les 3 requêtes sur les compétences : une seule
requête supplémentaire les charge toutes d'un coup (4 → 2).


# 4.3 Le piège
f - non , car Entreprise.objects.first() puis e.offres.all() donnent 2 requêtes. Pas de N+1, car e.offres.all() charge toutes les offres en une seule requête.

# Une panne à diagnostiquer
a - 


