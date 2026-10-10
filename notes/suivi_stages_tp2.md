### 1
Django repond No changes detected(il ne vois aucun changement),j'ai constater que Django identifie le modele par la modification du modele,sur ceux je peux endeduire que : une migration est une classe qui permet d'ajouter, modifier ou supprimer une entitée.
 

### 2
 On aura 03 trois tables en créer,Personne,parce que on peut pas recuperer tout les personne d'un seul coup.


### 3
- Non ya pas une table pour la classe personne,oui.
- 

### 4 
- Ce qui se passe : Django va lever une erreur de type          ProtectedError et refuser la suppression,  Oui elle a explicitement  stipulé « on ne perd jamais l’historique d’un stage... on doit pouvoir retrouver qui a fait quel stage, où, et avec qui »

- L'interface d'administration aurait affiché un écran de confirmation listant l'entreprise ainsi que les offres crées par cette entreprise,les candidature liées à ces offres et ses stages.



### 6
- 1-a  La création est acceptée par défaut par Django et la base de données. L'objet est enregistré en base sans erreur.

- 2-a La création est acceptée. En SQL, une chaîne vide ("") est une valeur textuelle valide, différente de NULL. À moins d'avoir restreint cela explicitement, la ligne est insérée.

- 3-a La création est refusée , à condition d'avoir respecté la consigne implicite de la responsable (« jamais deux fois à la même »).


- b Le probleme commun  1 et 2






