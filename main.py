import tkinter as tk

# Fonction pour afficher la grille dans l'interface
def afficher_grille_interface(grille):
    for i in range(6):
        for j in range(7):
            cell_value = grille[i][j]
            color = 'yellow' if cell_value == 'X' else 'red' if cell_value == 'O' else 'white'
            canvas.create_oval(j * 60 + 10, i * 60 + 10, (j + 1) * 60 - 10, (i + 1) * 60 - 10, fill=color)

# Fonction pour gérer le clic sur une colonne
def clic_colonne(colonne):
    global joueur_actuel, grille
    ligne = 5
    while grille[ligne][colonne] != ' ':
        ligne -= 1
    grille[ligne][colonne] = joueur_actuel

    afficher_grille_interface(grille)

    if verifier_victoire(grille, joueur_actuel, ligne, colonne):
        gagnant_label.config(text=f"Joueur {joueur_actuel} a gagné !")
        canvas.unbind("<Button-1>")
        return  # Ajoutez cette ligne pour quitter la fonction après la victoire

    coups_joues = sum(1 for row in grille for cell in row if cell != ' ')
    if coups_joues == 6 * 7:
        gagnant_label.config(text="Match nul !")
        canvas.unbind("<Button-1>")

    # Changer de joueur seulement si le jeu n'est pas encore terminé
    if gagnant_label.cget("text") == "":
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
        joueur_label.config(text=f"Joueur {joueur_actuel}")


# Fonction pour vérifier s'il y a un gagnant (similaire à la version précédente)
def verifier_victoire(grille, joueur, ligne, colonne):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Horizontale, verticale, diagonale droite, diagonale gauche

    for direction in directions:
        dx, dy = direction
        count = 1

        for i in range(1, 4):
            x, y = ligne + i * dx, colonne + i * dy
            if 0 <= x < 6 and 0 <= y < 7 and grille[x][y] == joueur:
                count += 1
            else:
                break

        for i in range(1, 4):
            x, y = ligne - i * dx, colonne - i * dy
            if 0 <= x < 6 and 0 <= y < 7 and grille[x][y] == joueur:
                count += 1
            else:
                break

        if count >= 4:
            return True

    return False


# Création de la fenêtre principale
root = tk.Tk()
root.title("Puissance 4")

# Création du canvas pour afficher la grille
canvas = tk.Canvas(root, width=420, height=360)
canvas.pack()

# Création des étiquettes pour les informations
joueur_actuel = 'X'
joueur_label = tk.Label(root, text=f"Joueur {joueur_actuel}", font=("Helvetica", 16))
joueur_label.pack()
gagnant_label = tk.Label(root, text="", font=("Helvetica", 16))
gagnant_label.pack()

# Initialisation de la grille
grille = [[' ' for _ in range(7)] for _ in range(6)]

# Affichage initial de la grille dans l'interface
afficher_grille_interface(grille)

# Liaison du clic de souris à la fonction de gestion
canvas.bind("<Button-1>", lambda event: clic_colonne(event.x // 60))


# Fonction pour recommencer une nouvelle partie
def recommencer_partie():
    global joueur_actuel, grille
    joueur_actuel = 'X'
    grille = [[' ' for _ in range(7)] for _ in range(6)]

    joueur_label.config(text=f"Joueur {joueur_actuel}")
    gagnant_label.config(text="")

    afficher_grille_interface(grille)
    canvas.bind("<Button-1>", lambda event: clic_colonne(event.x // 60))


# Création du bouton "Restart"
restart_button = tk.Button(root, text="Restart", command=recommencer_partie)
restart_button.pack()

# Lancement de la boucle principale
root.mainloop()