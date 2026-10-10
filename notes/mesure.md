Nombre d'offres : 3
sans rien : 7
avec select_related : 4
avec les deux : 2

# Explication
- `select_related("entreprise")` a supprimé les 3 requêtes sur l'entreprise : elle est chargée dans la même requête que l'offre, grâce à un JOIN (7 → 4).

- `prefetch_related("competence")` a supprimé les 3 requêtes sur les compétences : une seule
requête supplémentaire les charge toutes d'un coup (4 → 2).
