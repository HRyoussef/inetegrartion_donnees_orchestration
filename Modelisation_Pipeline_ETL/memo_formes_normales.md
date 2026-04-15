# Mémo : Formes Normales
## Appliquées au dataset entreprises Isère

## 1NF
Définition : chaque cellule contient une seule valeur atomique (pas de listes, pas de valeurs séparées par des virgules). Chaque ligne est unique.
Exemple de violation dans notre dataset : chaque cellule = une seule valeur. Dans notre dataset, adresse contient parfois rue + ville + CP collés ensemble → violation. Correction : séparer en colonnes distinctes.
Notre dataset est-il en 1NF ? non

## 2NF
Définition : en 1NF + tous les attributs dépendent de la TOTALITÉ de la clé primaire. Ne s applique qu aux clés composites. Si PK = siren (une colonne), 1NF implique automatiquement 2NF.
À quoi s'applique-t-elle ? pas de dépendance partielle sur une clé composite. Dans notre dataset, si on avait une PK (siren, nom_commune), le nom de l entreprise ne dépend que du siren → violation. Solution : table Entreprise avec PK = siren seul.
Notre dataset est-il en 2NF ? Oui

## 3NF
Définition : en 2NF + pas de dépendance transitive. `siren → code_naf → libelle_naf` est une violation. Solution : table Secteur séparée.
Violation dans notre dataset : Le libelle_naf dépend du code_naf, pas du siren
Solution appliquée : table Secteur(code_naf PK, libelle_naf)

## Conclusion
À quelle forme normale correspond le dataset plat ? Le diagramme v1 est en 2NF : les entités ont des PK simples et pas de dépendance partielle. 
À quelle forme normale correspond notre modèle cible (3 tables) ? 3NF
