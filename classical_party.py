from tkinter import *

fen = Tk()
fen.resizable(width=False, height=False)
fen.configure(bg ='#0002FF')
can = Canvas(fen,width= 692,height= 590, bg ="#0002FF")

fond_image_damier = PhotoImage(file ="image\damier.png" )
fond_image_pion_rouge = PhotoImage(file ="image\pion_rouge.png" )
fond_image_pion_jaune = PhotoImage(file ="image\pion_jaune.png" )

can.create_image(345,290,image = fond_image_damier)
can.create_image(100,100,image = fond_image_pion_rouge)
can.create_image(100,200,image = fond_image_pion_jaune)

can.pack()
fen.mainloop()