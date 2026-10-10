# TP — Vues, URLs, templates
## Une feuille de style 

a - Dans stages/static/stages/style.css, soit le dossier static/ de l’application, puis un sous-dossier portant le nom de l’application.
Le dossier static/ de l’application est trouvé automatiquement par Django (le finder AppDirectoriesFinder), sans configuration supplémentaire. Le fichier voyage avec l’application.



b - {% static %} construit l’adresse à partir de la configuration (STATIC_URL et le stockage choisi), au lieu de la figer dans le template. Cela rend possibles, en production :
    - Changer l’emplacement des fichiers sans toucher aux templates. Si les fichiers statiques passent sur un CDN ou un autre domaine (https://cdn.exemple.tg/static/), seul STATIC_URL change. Avec /static/... écrit en dur, il faudrait modifier chaque template.

# La correction
a - Le nom de l'erreur est : NoReverseMatch,elle survient au chargement de la page, pendant le rendu du template.

b - Comparaison avec une adresse écrite en dur
    . la page s’affiche normalement, sans aucune erreur côté serveur ;
    . le lien est mort : il mène à un 404, mais seulement quand quelqu’un clique ;

Je préfère NoReverseMatch, pour trois raisons :
- Elle est immédiate : dès qu’on charge la page, en développement, avant toute mise en ligne.

- Elle est bruyante et précise : Django indique le nom fautif, le template et la ligne.

- Elle protège l’utilisateur : l’erreur se découvre chez le développeur, pas chez le visiteur.