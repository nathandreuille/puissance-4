from tkinter import * # module qui permet de creer le jeux 
import random # module qui va nous permettre d'appeler la méthode randint pour choisir aléatoirement le joueur qui commence la partie

# programme puissance 4 :


# Définition d'une fonction qui lance une partie classique lorsqu'on appuie sur le bouton "partie classique" dans le menu principal.
def fct_classical_party ():
    global can, fen, player, checkerboard_list, couleur_code, couleur_joueur
    
    # Création de la fenêtre pour la partie classique.
    fen = Tk() 
    fen.configure(bg ="#CCD1D1") # Configuration de la couleur de fond de la fenêtre.
    fen.title("partie classique puissance 4") # Ajout d'un titre à la fenêtre.
    fen.resizable(width=False,height= False) # Configuration de la fenêtre pour qu'elle ne soit pas redimensionnable.
    can = Canvas(fen,height= 600, width=700, bg = "#000EEC") # Création d'un canvas de dimensions 700x600 avec une couleur de fond.
    can.pack()
    
    # Initialisation des variables.
    player = random.randint(1,2) # Le joueur qui commence est choisi aléatoirement.
    checkerboard_list = [[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3]] # Variable qui représente le damier du puissance 4. La valeur 3 permet de bloquer la descente du jeton à la dernière ligne.
    couleur_joueur=["gris","jaune","rouge"] # Couleurs des joueurs.
    couleur_code=["#AAAAAA","#FFEC00","#FF0000"] # Codes couleurs utilisés pour dessiner les jetons.
    
    # Ajout de widgets dans la fenêtre.
    label_player = Label(fen,text = "Le joueur "+couleur_joueur[player]+" commence la partie",font = "arial 16 bold").pack() # Affichage du joueur qui commence la partie.
    button_restart = Button(fen,text = "Recommencer ",font = "arial 16 bold",command =restart_game).pack() # Bouton pour recommencer la partie.
    button_menu = Button(fen,text = "Menu ",font = "arial 16 bold",command =fen.destroy).pack() # Bouton pour retourner au menu principal.
    button_replay = Button(fen,text = "↻",font = "arial 25 bold",command=fct_replay).place(x=50,y=620) # Bouton pour revenir un coup en arrière.
    label_explication_replay = Label (fen,text = "revenir un coup en arrière",font = "arial 8 bold").place(x=10,y=680) # Affichage d'une explication pour le bouton "revenir un coup en arrière".
    button_save = Button(fen,text = "Sauvegarder",font = "arial 16 bold",command=save_party).pack() # Bouton pour sauvegarder la partie.
    button_load = Button(fen,text = "Charger la partie sauvegardée",font = "arial 16 bold",command=load_party).pack() # Bouton pour charger une partie sauvegardée.
    checkerboard() # Génération du damier
    can.bind("<Button>",player_action) # méthode qui enregistre les clics de la souris 
    fen.mainloop() # mainloop permet de faire une boucle qui ne se termine pas tant qu'on ne ferme pas la fenetre comme un while == True tant qu'on appuie par sur la croix de la fenetre du jeu 
def fct_3set_party():
    pass
def checkerboard(): # fonction pour créer le damier du jeu (sous forme de dessin)
    x1 =0 # coordonnées en x du point gauche du rectangle 
    y1 = 0# coordonnées en y du point gauche du rectangle 
    x2 = 100# coordonnées en x du point droit du rectangle 
    y2 = 200# coordonnées en y du point droit du rectangle 
    for l in range(6):  # nombre de lignes
        for c in range(7): # nombre de colonnes 
            can.create_rectangle(x1,y1,x2,y2,width=5,outline="white") # méthode pour créer des rectangles (donc les carrés du damier)
            x1+=0
            x2+=100
        x1 = 0
        x2 = 100
        y1+=100
        y2+=100
def token(x1,y1,x2,y2,player): # fonction pour générer les pions des joueurs rouge joeur 2 jaune joueur 1 
    code=couleur_code[player]
    return can.create_oval(x1+10,y1+10,x2-10,y2-10,fill = code,width=3,outline = "white") # methode pour creer des formes ovales (donc en l'occurence les jetons)

def player_action(event): # fonction qui permet d'interpreter les entrées utilisateur (les clics de souris des joueurs)
    global player,checkerboard_list,can,col,line,id_token
    X = event.x # cordonnées en X du clic 
    Y = event.y # cordonnés en Y du clic 
    col = X//100 # on fait la division euclidienne pour recuperer la colone du clic qui sont numérotées de 1 à 6
    line = Y//100 # on fait la division euclidienne pour recuperer la ligne du clic qui sont numérotées de 1 à 7
    id_checkerboard = [col,line] # variable qui récuperer sous forme de liste la colonne et la ligne de l'entrée utilisateur 
    
    while checkerboard_list[col][line+1]==0: # pour faire descendre le jeton dans le damier jusqu'à qu'il y en ait un en dessous d'ou l'interet du 3 dans la liste qui empeche le jeton de desendre plus bas que le damier
            line+=1
        
    while checkerboard_list[col][line]!=0 and line>=0  : # empecher de changer la couleur d'un pion qui est deja placé dans le damier
            line-=1    
    checkerboard_list[col][line] = player # remplir le damier quand un joueur joue 
    if player ==1 or player == 2:
        id_token = token(col*100,line*100,col*100+100,line*100+100,player) # on appelle la fonction pour créer un jeton et on change la couleur en fonction du "player" 
        
    if fct_equality(): # fonction qui test si il n'y a plus de place dans le damier et donc egalité
        label_equality= Label(fen,text = "Egalité entre les 2 joueurs !",font= "arial 20 bold",bg ="#000EEC", fg ="black" )
        label_equality.place(x = 210,y=285)
        fen.after(3000, fen.destroy)
        
    if fct_line_winner() or fct_column_winner() or fct_diagonal_winner() : # controler si un joueur a alligné 4 jetons (en diagonale,ligne,colonne)
        if player == 1 or player == 2:
            label_yellow_winner = Label(fen,text = "Le joueur "+couleur_joueur[player]+" a gagné",font= "arial 20 bold",bg =couleur_code[player], fg ="white" )
            label_yellow_winner.place(x = 210,y=285)
            fen.after(3000, fen.destroy) # fermer la fenetre après une victoire
            player = -1 # empecher de joueur une fois la partie terminée 
    if player==1: # changement du joueur 
        player=2
    elif player==2:
        player=1
    else :
         pass
    
def restart_game():  # fonction pour recommencer la partie quand on clique sur le bouton "recommencer"
    fen.destroy()
    fct_classical_party()

def save_party(): # fonction pour enregistrer le damier dans le fichier save_party 
    global folder,can
    with open("save_party.txt", "w") as folder:
        for sous_liste in checkerboard_list:
            for nombre in sous_liste:
                folder.write(str(nombre) + " ")
            folder.write("\n")
    
def load_party(): # fonction pour charger la partie après la souvegarde 
    global folder ,can,checkerboard_list,line,col,id_token
    checkerboard_list = []
    can.delete("all")
    checkerboard()
    with open("save_party.txt", "r") as folder:
        ligne = folder.readline()
        while ligne: # pour transformer la damier qui est enregistré en str dans le fichier en int pour que les valeurs soit exploitables
            entiers = [int(nombre) for nombre in ligne.strip().split()]
            checkerboard_list.append(entiers)
            ligne = folder.readline()
    for col in range(7): # test colonne 
         for line in range(6): # test lignes 
            if checkerboard_list[col][line] == 1: # placer un pion jaune si il y a un 1
                id_token = token(col*100,line*100,col*100+100,line*100+100,1)
            elif checkerboard_list[col][line] == 2: # placer un pion rouge si il y a un 2
                id_token = token(col*100,line*100,col*100+100,line*100+100,2)
            else:
                pass


def fct_replay(): # fonction pour revenir un coup en arriere si l'on s'est trompé en jouant 
    global player,checkerboard_list
    if not(fct_line_winner() or fct_column_winner() or fct_diagonal_winner()):    
        can.delete(id_token) # methode pour supprimer le pion du damier 
        checkerboard_list[col][line]= 0
        if player == 1:
            player = 2
        else :
            player=1


def fct_equality(): # fonction pour controler si il y a égalité on regarde si il a un 0 c'est à dire encore une place libre dans la liste du damier
    global checkerboard_list
    a =0
    if a in checkerboard_list[0]  or a in checkerboard_list[1] or a in checkerboard_list[2] or a in checkerboard_list[3] or a in checkerboard_list[4] or a in checkerboard_list[5] or a in checkerboard_list[6]: 
        equality = False 
    else :
        equality =True 
    return equality


def fct_line_winner(): # fonction pour controler si un joueur a fait une ligne de 4 return true si il y a un gagnant 
    winner = False 
    for i in range(6):
        for a in range(4):
            if checkerboard_list[a][i]==checkerboard_list[a+1][i]==checkerboard_list[a+2][i]==checkerboard_list[a+3][i] and checkerboard_list[a][i]+checkerboard_list[a+1][i]+checkerboard_list[a+2][i]+checkerboard_list[a+3][i]!=0:
                winner = True
    return winner 

def fct_column_winner(): #fonction pour controler si un joueur a fait une colonne de 4 return true si il y a un gagnant
    winner = False
    for i in range(7):
        for a in range(4):
            if checkerboard_list[i][a] == checkerboard_list[i][a+1]==checkerboard_list[i][a+2]==checkerboard_list[i][a+3] and checkerboard_list[i][a] +checkerboard_list[i][a+1]+checkerboard_list[i][a+2] + checkerboard_list[i][a+3]!=0:
                winner = True
    return winner

        
def fct_diagonal_winner(): #fonction pour controler si un joueur a fait une diagonale de 4 return true si il y a un gagnant
    winner = False
    for i in range(3):
        for a in range(3,7):  
            if checkerboard_list[a][i]==checkerboard_list[a-1][i+1]==checkerboard_list[a-2][i+2]==checkerboard_list[a-3][i+3] and checkerboard_list[a][i]+checkerboard_list[a-1][i+1]+checkerboard_list[a-2][i+2]+checkerboard_list[a-3][i+3]!=0:
                winner = True 
    for i in range(3):
        for a in range(4):
                if checkerboard_list[a][i]==checkerboard_list[a+1][i+1]==checkerboard_list[a+2][i+2]==checkerboard_list[a+3][i+3] and checkerboard_list[a][i]+checkerboard_list[a+1][i+1]+checkerboard_list[a+2][i+2]+checkerboard_list[a+3][i+3]!=0:
                    winner = True
    return winner

windows = Tk() # fenetre du  menu principal 
# configuration de la fenetre du menu 
windows.title ("puissance 4") # titre du jeu
windows.configure(bg ='#CCD1D1') # couleur menu principal 
windows.resizable(width=False,height= False)
can = Canvas(windows, width = 500, height = 500, bg ="white")
font = 'arial 13 bold' # ecriture en gras
boutton_3manches = Button(windows,text = "Commencer une partie en 3 manches",font = font, fg = "black", bg = 'white',command=fct_3set_party) # button permet de "pack" un bouton sur la canvas (fenetre ou l'on interagit)
boutton_classique = Button(windows,text = 'Commencer une partie classique',font = font, fg = "black", bg = 'white',command = fct_classical_party) # on appelle la fonction fct_classical party pour lancer la partie lorsque le bouton est pressé 
quit = Button(windows, text="Annuler", font = font,fg ="black",bg ="white", command = windows.destroy ) # fermer la fenetre quanbd on appuie sur le bouton annuler
fond_image = PhotoImage(file = "image/2.png") # affichage de l'image(image du menu )
can.create_image(260,250, image = fond_image)
can.pack() 
boutton_classique.pack()
boutton_3manches.pack()
quit.pack()

windows.mainloop() # boucle du jeu 