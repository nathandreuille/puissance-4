from tkinter import * # module qui permet de creer le jeux 
import random # module qui va nous permettre d'appeler la méthode randint pour choisir aléatoirement le joueur qui commence la partie

# programme puissance 4 :

def fct_classical_party ():  # fonction qui permet de lancer une partie classique lorsque l'on appuie sur le bouton partie classique dans le menu pricipal 
    global can,fen,player,checkerboard_list,label_player,red_score,yellow_score
    fen = Tk() # fenetre partie classique 
    # configuration de la fenetre de la partie classique 
    fen.title("partie classique puissance 4")
    fen.resizable(width=False,height= False)
    can = Canvas(fen,height= 600, width=700, bg = "#000EEC")
    can.pack()
    player = random.randint(1,2) # 1 : jaune , 2 : rouge , la méthode random permet de chosir aléatoirement la joueur qui débute 
    red_score, yellow_score = 0,0
    checkerboard_list = [[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3]] # variable qui represente le damier du puissance 4 la valeur 3 permet de bloquer la descente du jeton à la derniere ligne(suite du programme)
    replay = False 
    if player == 1:
        label_player = Label(fen,text = "Le joueur jaune commence la partie", font = "arial 16 bold")
        
    else :   
        label_player = Label(fen,text = "Le joueur rouge commence la partie",font = "arial 16 bold")
    
    label_player.pack()
    button_restart = Button(fen,text = "Recommencer ",font = "arial 16 bold",command =restart_game)
    button_menu = Button(fen,text = "Menu ",font = "arial 16 bold",command =fen.destroy)
    button_replay = Button(fen,text = "↻",font = "arial 25 bold",command=fct_replay)
    button_restart.pack()
    button_menu.pack()
    button_replay.pack()
    checkerboard() # on appelle la fonction pour generer le damier de jeu 
    can.bind("<Button>",player_action) # méthode qui enregistre les clics de la souris 
    fen.mainloop() # mainloop permet de faire une boucle qui ne se termine pas tant qu'on ne ferme pas la fenetre comme un while == True tant qu'on appuie par sur la croix de la fenetre du jeu 

def fct_3set_party():
    pass

def checkerboard(): # fonction pour créer le damier du jeu (sous forme de dessin)
    x1 =0
    y1 = 0
    x2 = 100
    y2 = 100
    for x in range(6):  # nombre de colones 
        for i in range(7): # nombre de lignes 
            can.create_rectangle(x1,y1,x2,y2,outline = "white",width=5) # méthode pour créer des rectangles (donc les carrés du damier)
            x1+=100
            x2+=100
        x1 =0
        y1+=100
        y2+=100


def red_token(x1,y1,x2,y2): # fonction pour générer les pions rouges 
    return can.create_oval(x1+10,y1+10,x2-10,y2-10,fill = "#FF0000",width=3,outline = "white") # methode pour creer des formes ovales (donc en l'occurence les jetons)
    

def yellow_token(x1,y1,x2,y2): # fonction pour générer les pions jaunes 
    return can.create_oval(x1+10,y1+10,x2-10,y2-10,fill = "#FFEC00",width=3,outline = "white")

def player_action(event): # fonction qui permet d'interpreter les entrées utilisateur (les clics de souris des joueurs)
    global player,checkerboard_list, red_score,yellow_score,can,col,line,id_yellow_token,id_red_token
    
    X = event.x # cordonnées en X du clic 
    Y = event.y # cordonnés en Y du clic 
    col = X//100 # on fait la division euclidienne pour recuperer la colone du clic qui sont numérotées de 1 à 6
    line = Y//100 # on fait la division euclidienne pour recuperer la ligne du clic qui sont numérotées de 1 à 7
    id_checkerboard = [col,line] # variable qui récupere sous forme de liste la colonne et la ligne de l'entrée utilisateur 
    
    
    if player == 1: # actions du joueur jaune 
        
        while checkerboard_list[col][line+1]==0: # pour faire descendre le jeton dans le damier jusqu'à qu'il y en ait un en dessous d'ou l'interet du 3 dans la liste qui empeche le jeton de desendre plus bas que le damier
            line+=1
        
        while checkerboard_list[col][line]!=0: # empecher de changer la couleur d'un pion qui est deja placé dans le damier
            line-=1    
        checkerboard_list[col][line] = 1
        id_yellow_token = yellow_token(col*100,line*100,col*100+100,line*100+100) # on appelle la fonction pour créer un jeton jaune 
        
       
         # changement de joueur dans ce cas on passe du tour du joueur jaune au tour du joueur rouge
       
        player = 2    
        if fct_equality(): # 42 soit 6*7 permet d'arreter le jeu lorsqu'il y a égalité entre les 2 joueurs c'est à dire quand tous les trous du damier sont occcupés 
            label_equality= Label(fen,text = "Egalité entre les 2 joueurs !",font= "arial 20 bold",bg ="#000EEC", fg ="black" )
            label_equality.place(x = 210,y=285)
            fen.after(3000, fen.destroy)
        
        if fct_line_winner() or fct_column_winner() or fct_diagonal_winner(): # controler si un joueur a alligné 4 jetons
            label_yellow_winner = Label(fen,text = "Le joueur jaune a gagné",font= "arial 20 bold",bg ="#FFEC00", fg ="white" )
            label_yellow_winner.place(x = 210,y=285)
            yellow_score +=1
            fen.after(3000, fen.destroy) # fermer la fenetre après une victoire
            player = 0
    
    elif player == 2: # actions du joueur rouge 
        while checkerboard_list[col][line+1]==0:
            line+=1
        while checkerboard_list[col][line]!=0:
            line-=1
        checkerboard_list[col][line] = 2
        id_red_token=red_token(col*100,line*100,col*100+100,line*100+100)
        player = 1
        
        
            

        if fct_equality(): # fonction qui teste si il y a encore de la place dans le damier
            label_equality= Label(fen,text = "Egalité entre les 2 joueurs !",font= "arial 20 bold",bg ="#000EEC", fg ="white" )
            label_equality.place(x = 210,y=285)
            fen.after(3000, fen.destroy)
        
        if fct_line_winner() or fct_column_winner() or fct_diagonal_winner():
            label_red_winner = Label(fen,text = "Le joueur rouge a gagné",font= "arial 20 bold", bg = "#FF0000",fg ="black")
            label_red_winner.place(x = 210,y=285)
            red_score +=1
            player= 0
            fen.after(3000, fen.destroy)
        
        

def restart_game():  # fonction pour recommencer la partie quand on clique sur le bouton "recommencer"
    fen.destroy()
    fct_classical_party()



def fct_replay():
    global player,checkerboard_list
    if player == 1:
        player = 2
        can.delete(id_red_token)
    else :
        can.delete(id_yellow_token)
        player = 1
    checkerboard_list[col][line]= 0
   
   
    


def fct_equality():
    global checkerboard_list
    a =0
    if a in checkerboard_list[0]  or a in checkerboard_list[1] or a in checkerboard_list[2] or a in checkerboard_list[3] or a in checkerboard_list[4] or a in checkerboard_list[5] or a in checkerboard_list[6]: 
        equality = False 
    else :
        equality =True 
    return equality


def fct_line_winner(): # fonction pour controler si un joueur a fait une ligne de 4
    winner = False 
    for i in range(6):
        for a in range(4):
            if checkerboard_list[a][i]==checkerboard_list[a+1][i]==checkerboard_list[a+2][i]==checkerboard_list[a+3][i] and checkerboard_list[a][i]+checkerboard_list[a+1][i]+checkerboard_list[a+2][i]+checkerboard_list[a+3][i]!=0:
                winner = True
    return winner 
        
def fct_column_winner(): #fonction pour controler si un joueur a fait une colonne de 4
    winner = False
    for i in range(7):
        for a in range(4):
            if checkerboard_list[i][a] == checkerboard_list[i][a+1]==checkerboard_list[i][a+2]==checkerboard_list[i][a+3] and checkerboard_list[i][a] +checkerboard_list[i][a+1]+checkerboard_list[i][a+2] + checkerboard_list[i][a+3]!=0:
                winner = True
                
    return winner

def fct_diagonal_winner(): #fonction pour controler si un joueur a fait une diagonale de 4
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
windows.title ("puissance 4")
windows.configure(bg ='white')
can = Canvas(windows, width = 500, height = 500, bg ="white")
font = 'arial 13 bold' # ecriture en gras
boutton_3manches = Button(windows,text = "Commencer une partie en 3 manches",font = font, fg = "black", bg = 'white',command=fct_3set_party) # button permet de "pack" un bouton sur la canvas (fenetre ou l'on interagit)
boutton_classique = Button(windows,text = 'Commencer une partie classique',font = font, fg = "black", bg = 'white',command = fct_classical_party) # on appelle la fonction fct_classical party pour lancer la partie lorsque le bouton est pressé 
quit = Button(windows, text="Annuler", font = font,fg ="black",bg ="white", command = windows.destroy ) # fermer la fenetre quanbd on appuie sur le bouton annuler
frame = Frame (windows, bg = "white")
fond_image = PhotoImage(file = "image/2.png") # affichage de l'image genere par l'intelligence artificielle (image du menu )
can.create_image(260,250, image = fond_image)
can.pack() 
boutton_classique.pack()
boutton_3manches.pack()
can.bind( )
frame.place(x = 130 , y = 130)
quit.pack()
windows.mainloop()