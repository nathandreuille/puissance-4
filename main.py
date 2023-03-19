from tkinter import *

windows = Tk()
windows.title ("puissance 4")
windows.geometry('400x400+450+250')
windows.configure(bg ='white')

can = Canvas(windows, width = 300, height = 300, bg ="#2596be")
font = 'arial 13 bold' # ecriture en gras
boutton_3manches = Button(windows,text = "Commencer une partie en 3 manches",font = font, fg = "black", bg = 'white')
boutton_classique = Button(windows,text = 'Commencer une partie classique',font = font, fg = "black", bg = 'white')
quit = Button(windows, text="Annuler", font = font,fg ="black",bg ="white", command = quit )
label = Label(windows,text = "Bonjour bienvenu \n sur le puissance 4 de \n Nathan, Brian et Adrien", font = "arial 13 bold", bg = "white", fg = "black")
can.pack()
boutton_classique.pack()
boutton_3manches.pack()
can.bind( )
label.place(x = 100, y = 100)
quit.pack()
windows.mainloop()