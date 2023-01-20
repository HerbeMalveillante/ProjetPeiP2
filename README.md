# ProjetPeiP2 - Jeu de NIM

> Année : 2023
>
> Mots-clés : Informatique
> Programmation
> Mathématiques Appliquées
> Intelligence artificielle
>
> Encadrant : DI BILLAUT Jean-Charles

## Projet Nim

Les jeux de Nim sont des jeux de stratégie pure. Il en existe plusieurs variantes. Ils se jouent avec des graines, des billes, des jetons, des allumettes ou tout autre objet facilement manipulable. Ce sont des jeux à 2 joueurs.

https://fr.wikipedia.org/wiki/Jeux_de_Nim

On considèrera un jeu de Nim qui ressemble au jeu de Morpion sur un plateau n x n.
A chaque tour, un joueur peut mettre 1, 2, 3, ... ou n croix, mais dans la même ligne ou la même colonne.
Le joueur qui met la (ou les) dernière(s) croix a gagné.

But du projet :

-   Réaliser une interface graphique permettant à un joueur de jouer, et détecter une victoire
-   Réaliser une IA qui gagne systématiquement

Programmation :
Python, interface Tkinter

### Première séance

Chaque grille valide est divisée en deux groupes : le noyau et le reste. Quand c'est à notre tour de jouer et que la grille est dans le noyau, on a automatiquement perdu.
Le but étant de jouer un coup qui amène la grille dans le noyau pour le tour du joueur adverse.

On doit donc trouver quel est le dit noyau et y retourner à chaque coup. Le joueur qui commence contre un joueur "parfait" gagne donc systématiquement.

Les grilles sont représentées sous forme de graphe : chaque grille est associée aux grilles qui peuvent être obtenues en jouant un coup. De ce fait on peut utiliser un algorithme pour déterminer si une grille fait partie du noyau ou non, et donc la choisir parmi les grilles possibles.

La symétrie est importante : on peut donc réduire le nombre de grilles à étudier en ne considérant que les grilles symétriques.

-> Déroulement d'une partie :

En boucle :

1. On considère la grille que le robot doit jouer.
2. On regarde toutes les grilles que le robot peut jouer.
3. On en sélectionne une qui est dans le noyau (si elle existe).
4. Si aucune grille n'est dans le noyau, on sélectionne une grille qui n'est pas dans le noyau en esperant que le joueur reste en dehors de celui-ci.

Ce qui est important en somme :

1. trouver un moyen de représenter les grilles
2. trouver tout le bail de symétrie
3. trouver un algorithme pour déterminer si une grille est dans le noyau ou non (par extension trouver un algorithme qui permet de trouver le noyau dès le départ)
4. Coder l'interface et la boucle de jeu

#### symétries :

Il y a une liste finie de symétries.

1. rotation de 90°
2. rotation de 180°
3. rotation de 270°
4. symétrie horizontale
5. symétrie verticale

Donc il faut coder deux fonctions :

1. Une fonction qui tourne le plateau à 90° (qu'on peut lancer deux ou trois fois pour 180 et 270°)
2. Une fonction qui fait une symétrie horizontale.

à partir de ça, on peut avoir toutes les symétries possibles :

Rotation 90° = 1x(1)
Rotation 180° = 2x(1)
Rotation 270° = 3x(1)
Symétrie horizontale = 1x(2)
Symétrie verticale = 1x(2) + 2x(1)

Si on doit coder un algorithme pour pivoter une grille de 90° (dans le sens des aiguilles d'une montre, arbitrairement) de dimension n\*n, voilà ce qu'on peut faire :

-   On crée une grille vide de dimension n\*n vide
-   On parcourt la grille de gauche à droite, de haut en bas (donc bit par bit dans la représentation binaire)
-   Pour chaque bit, on récupère sa ligne et sa colonne. Sa ligne correspond au lot de n bits dans lequel il se situe (exemple pour une grille 3x3, la ligne 1 contient les 3 premiers bits, la ligne 2 correspond aux bits 4, 5 et 6, etc.). Sa colonne se calcule en calculant sa position dans son lot de bits (donc en faisant la position globale dans la grille modulo n).
-   On calcule ensuite la nouvelle position du bit dans la grille. Pour cela, on calcule la nouvelle ligne et la nouvelle colonne. La nouvelle ligne est la colonne de l'ancien bit, et la nouvelle colonne est n - 1 - la ligne de l'ancien bit.
-   On fait la même chose pour chaque bit de la grille, et on obtient la grille tournée de 90°.

Si on doit coder un algorithme pour faire une symétrie horizontale, voilà ce qu'on peut faire :

-   On crée une grille vide de dimension n\*n vide
-   On parcourt la grille de gauche à droite, de haut en bas (donc bit par bit dans la représentation binaire)
-   Pour chaque bit, on récupère sa ligne et sa colonne. Sa ligne correspond au lot de n bits dans lequel il se situe (exemple pour une grille 3x3, la ligne 1 contient les 3 premiers bits, la ligne 2 correspond aux bits 4, 5 et 6, etc.). Sa colonne se calcule en calculant sa position dans son lot de bits (donc en faisant la position globale dans la grille modulo n).
-   On calcule ensuite la nouvelle position du bit dans la grille. Pour cela, on calcule la nouvelle ligne et la nouvelle colonne. La nouvelle colonne est (n + 1) - la colonne de l'ancien bit, et la nouvelle ligne est la même.

À partir de ces deux algorithmes, on peut facilement trouver toutes les symétries d'une grille.
Pour prouver que deux grilles sont symétriques, on génère toutes les symétries d'une grille et on vérifie que la grille B est dans la liste des symétriques de la grille A

COMPTE RENDU FIN DE SÉANCE :

Nous avons écrit un résumé de ce que nous allons devoir comprendre et implémenter afin de mener à bien ce projet, nous avons finalement écrit une partie du code permettant de générer tous les symétriques d'une grille de dimension n avec une représentation binaire.
