Le modele Entreprise
La specification

1 - La combinaison de champs identifiant une entreprise est : nom et la ville,non une seule entreprise.


2 - L’adresse mail est du type EmailField,il doit pas etre simplement du type texte car Django valide le format automatiquement saisie dans l'admin pour eviter les adresse bizzare.


3 - 

4 - La dernière phrase du secrétariat parle de l'affichage de l'entreprise : __str__(),quand Django affiche quelque chose c' est cette methode qui est appelé.


Migration
a - La contrainte s'appelle UNIQUE.

b - La colonne est id,par defaut Django cré automatiquement cette colonne id qui permet d'identifier chaque ligne dans la base de donnée.

c - Apres la modification du model on constate que on a au total 2 fichiers de migrations,pour revenir en arriere il faudra qu'on fais un rollback avec la commande uv run manage.py migrate stages 0001(on reapplique la migration 0001 et annule 0002 mais elle existe sur le disque il faut quon le supprime manuellement).


4 L'administration 
a - L'erreur apparait en validant(lors de l'enregistrement par ce que une entreprise existe deja avec ce nom).

b - Oui

5 - La premiere page 
a - Elle liste l'erreur d'inexistance de ce chemin,il dit qu'il ne retrouve pas le fichier liste_entreprises.html et quelle doit ce retouver dans   /home/lafaouyi/suivi_stages/.venv/lib/python3.14/site-packages/django/contrib/auth/templates/stages/liste_entreprises.html


b - non,car en production la variable DEBUG passe à False( DEBUG=False)

6-Le depot git 
a - cest la base de donnée db.sqlite3,parce que en production utilise PostgreSQL ou MySQL,pas sqlite

b - Deux fichiers engendrés par uv : uv.lock et pyproject.toml,ils servent de faire uv sync(reconstruit exactement le meme environement que le projet) 




