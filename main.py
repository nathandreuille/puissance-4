from tkinter import *

windows = Tk()
windows.title ("puissance 4")
windows.geometry('400x400+450+250')
windows.configure(bg ='white')

def classical_party ():
    damier = PhotoImage(file = "image/damier.png")
    label_damier = Label (windows,image = damier)
    label_damier.pack()
    windows.mainloop()

can = Canvas(windows, width = 300, height = 300, bg ="#2725BE")
font = 'arial 13 bold' # ecriture en gras
boutton_3manches = Button(windows,text = "Commencer une partie en 3 manches",font = font, fg = "black", bg = 'white')
boutton_classique = Button(windows,text = 'Commencer une partie classique',font = font, fg = "black", bg = 'white',command=classical_party)
quit = Button(windows, text="Annuler", font = font,fg ="black",bg ="white", command = quit )
frame = Frame (windows, bg = "white")
label = Label(frame ,text = "Puissance", font = "arial 20 bold", bg = "white", fg = "#FF0000")
label2 = Label(frame, text = "4", font = "arial 20 bold", bg = "white", fg = "#FFF000")
can.pack()
boutton_classique.pack()
boutton_3manches.pack()
can.bind( )
label.pack()
label2.pack()
frame.place(x = 130 , y = 130)
quit.pack()
windows.mainloop()