from tkinter import *
import random 
"""def fct_classical_party ():
    global can,fen,player,checkerboard_list
    fen = Tk()
    fen.title("partie classique puissance 4")
    fen.resizable(width=False,height= False)
    can = Canvas(fen,height= 600, width=700, bg = "#000EEC")
    can.pack()
    player = random.randint(1,2) # 1 : jaune , 2 : rouge
    checkerboard_list = [[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3],[0,0,0,0,0,0,3]]
    if player == 1:
        label = Label(fen,text = "Le joueur jaune commence", font = "arial 16 bold")
    else :   
        label = Label(fen,text = "Le joueur rouge commence",font = "arial 16 bold")
    label.pack()
    can.bind("<Button>",clic)
    checkerboard()
    fen.mainloop()


def checkerboard(): 
    x1 =0
    y1 = 0
    x2 = 100
    y2 = 100
    for x in range(6):  
        for i in range(7):
            can.create_rectangle(x1,y1,x2,y2,width=5)
            x1+=100
            x2+=100
        x1 =0
        y1+=100
        y2+=100


def red_token(x1,y1,x2,y2):
    can.create_oval(x1+10,y1+10,x2-10,y2-10,fill = "#FF0000",width=3)


def yellow_token(x1,y1,x2,y2):
    can.create_oval(x1+10,y1+10,x2-10,y2-10,fill = "#4DFF00",width=3)

def clic(event):
    global player,checkerboard_list
    X = event.x
    Y = event.y
    col = X //100
    line = Y//100
    id_checkerboard = [col,line]
    
    if player == 1:
        while checkerboard_list[col][line+1]==0:
            line+=1

        checkerboard_list[col][line] = 1
        yellow_token(col*100,line*100,col*100+100,line*100+100)
        player = 2
        
    else:
        while checkerboard_list[col][line+1]==0:
            line+=1
        checkerboard_list[col][line] = 2
        red_token(col*100,line*100,col*100+100,line*100+100)
        player = 1


fct_classical_party()"""


def fct_equality():
    checkerboard_list = [[1,1,1,1,1,1,3],[1,1,1,1,1,1,3],[1,1,1,1,1,1,3],[1,1,1,1,1,1,3],[1,1,1,1,1,1,3],[1,1,1,1,1,1,3],[1,1,1,1,1,1,3]]
   
    a =0
    if a in checkerboard_list[0]  or a in checkerboard_list[1] or a in checkerboard_list[2] or a in checkerboard_list[3] or a in checkerboard_list[4] or a in checkerboard_list[5] or a in checkerboard_list[6]: 
        equality = False 
    else :
        equality =True 
    return equality
print(fct_equality())