from tkinter import *
import random 
fen = Tk()
fen.title("partie classique puissance 4")
fen.resizable(width=False,height= False)
can = Canvas(fen,height= 600, width=700, bg = "#000EEC")
can.pack()
player = random.randint(1,2) # 1 : jaune , 2 : rouge

if player == 1:
    label = Label(fen,text = "Le joueur jaune commence", font = "arial 16 bold")
else :   
    label = Label(fen,text = "Le joueur rouge commence",font = "arial 16 bold")
label.pack()


def checkerboard(): 
    x1 =0
    y1 = 0
    x2 = 100
    y2 = 100
    for x in range(6):  
        for i in range(7):
            can.create_rectangle(x1,y1,x2,y2)
            x1+=100
            x2+=100
        x1 =0
        y1+=100
        y2+=100


def red_token(x1,y1,x2,y2):
    can.create_oval(x1,y1,x2,y2,fill = "red")


def yellow_token(x1,y1,x2,y2):
    can.create_oval(x1,y1,x2,y2,fill = "yellow")

def clic(event):
    global player
    X = event.x
    Y = event.y
    col = X //100
    line = Y//100
    if player == 1:
        yellow_token(col*100,line*100,col*100+100,line*100+100)
        player = 2
    else:
        red_token(col*100,line*100,col*100+100,line*100+100)
        player = 1


can.bind("<Button>",clic)
        



checkerboard()





fen.mainloop()



