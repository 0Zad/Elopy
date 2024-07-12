# ELOpy
ELOpy est un outil de calcul de côte Elo

# Installation 
Récupération des sources et installation des dépendances
```
git clone
cd
pip install -r requirements.txt
```

# Utilisation
## Ajouter un match

Pour ajouter un match il faut editer le fichier "matchs.txt" : avec le nom des joueurs suivent de leur classement. Dans l'exemple ci dessous le joueurs player_3 à gagné et player_1 à fini dernier.
```
player_1 player_2 player_3 player_4 player_3 player_4 player_2 player_1
```
Il possible d'ajouter des matchs à deux, trois ou quatre joueurs.

## Ajouter une équipe

Pour ajouter une équipe il faut éditer le fichier "equipes.txt" sur le format suivante :
```
equipe_name : player_1 player_2
```
## Afficher les résultats via streamlite
```
streamlit run ./ELO.py
```
Les boutons "Individuel" et "Equipes" permettent de recalculer et d'afficher, respectivement, le classement individuel et par équipe.

# Theory

Le calcul de la coté se base sur le principe d'Arpad Elo et utiliser initalement pour les échecs.
Ra = Ra + K*(Sa - Ea) avec :
- Ea = Qa /(Qa + Qb), Qa = 10^(Ra/c), Qb = 10^(Rb/c), 0 ≤ Ea ≤ 1.
- Sa est le résultat du match. Sa = (n-k)/(n-1) pour n le nombre de joueur et k la position au classement.