Puissance 4 - Jeu en Python avec Tkinter
Ce projet est une implémentation simple du jeu de Puissance 4 en utilisant Python et la bibliothèque Tkinter pour l'interface graphique. Le jeu se joue à deux joueurs, l'un utilisant les jetons "X" et l'autre les jetons "O". Le but du jeu est d'aligner quatre jetons horizontalement, verticalement ou en diagonale avant son adversaire.

Fonctionnalités
Interface graphique : Le jeu est entièrement jouable via une interface graphique intuitive.

Joueur contre joueur : Deux joueurs peuvent jouer l'un contre l'autre en alternant les tours.

Détection de victoire : Le jeu détecte automatiquement lorsqu'un joueur a aligné quatre jetons et déclare le gagnant.

Match nul : Si la grille est remplie sans qu'aucun joueur n'ait aligné quatre jetons, le jeu déclare un match nul.

Bouton "Restart" : Un bouton permet de recommencer une nouvelle partie à tout moment.

Comment jouer
Lancer le jeu : Exécutez le script Python pour démarrer le jeu.

Jouer un coup : Cliquez sur la colonne où vous souhaitez placer votre jeton. Le jeton tombera automatiquement à la position la plus basse disponible dans cette colonne.

Alternance des joueurs : Les joueurs alternent les tours, avec "X" commençant toujours en premier.

Victoire ou match nul : Le jeu détecte automatiquement si un joueur a gagné ou si la grille est remplie sans gagnant (match nul).

Recommencer : Cliquez sur le bouton "Restart" pour recommencer une nouvelle partie.

Structure du code
afficher_grille_interface(grille) : Cette fonction affiche la grille de jeu dans l'interface graphique. Les jetons "X" sont affichés en jaune, les jetons "O" en rouge, et les cases vides en blanc.

clic_colonne(colonne) : Cette fonction gère le clic sur une colonne. Elle place le jeton du joueur actuel dans la colonne sélectionnée et vérifie si ce coup entraîne une victoire ou un match nul.

verifier_victoire(grille, joueur, ligne, colonne) : Cette fonction vérifie si le dernier coup joué a entraîné une victoire pour le joueur actuel.

recommencer_partie() : Cette fonction réinitialise la grille et les étiquettes pour commencer une nouvelle partie.

Dépendances
Python 3.x : Le script est écrit pour Python 3.

Tkinter : La bibliothèque Tkinter est utilisée pour l'interface graphique. Elle est généralement incluse avec Python.

Exécution
Pour exécuter le jeu, assurez-vous d'avoir Python installé, puis exécutez le script suivant dans votre terminal ou environnement de développement :

bash
Copy
python puissance4.py
Améliorations possibles
Interface améliorée : Ajouter des animations ou des effets visuels pour rendre le jeu plus attractif.

Mode solo : Implémenter une IA pour permettre à un joueur de jouer contre l'ordinateur.

Sauvegarde de partie : Ajouter une fonctionnalité pour sauvegarder et charger une partie en cours.
