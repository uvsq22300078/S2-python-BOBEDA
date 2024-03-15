import tkinter as tk
import random

coul = "black"

def changeCouleur ():
    couleu = input("Input color")
    global coul
    coul = couleu

def cercle ():
    x = random.randint(0,600-50)
    y = random.randint(0,400-50)
    diametre = 50
    canva.create_oval(x,y,x+diametre,y+diametre,fill=coul)

def carre ():
    x = random.randint(0,600-50)
    y = random.randint(0,400-50)
    print("yes")
    canva.create_rectangle(x,y,x+50,y+50,fill=coul)

def ligne():
    cordx= random.randint(50,400-50)
    cordy = random.randint(50,600-50)
    canva.create_line(cordx, cordy-50, cordx,cordy+50, fill=coul)
    canva.create_line(cordx+50, cordy, cordx-50,cordy, fill=coul)

root = tk.Tk(className="dessin")

canva = tk.Canvas(root,width= 600,height=400)
buttonCouleur = tk.Button(root, text="Changer couleur",command=changeCouleur)
buttonCerle = tk.Button(root, text="cercle",command=cercle)
buttonCarre = tk.Button(root, text="Carre",command=carre)
buttonCroix = tk.Button(root, text="Croix",command=ligne)

canva.grid(row=1,column=1)
buttonCouleur.grid(row=0,column=1)
buttonCerle.grid(row=1,column=0)
buttonCarre.grid(row =2, column=0)
buttonCroix.grid(row=3,column=0)
root.mainloop()