import tkinter as tk
import random

couleur = ["black","red","white","green"]
def coul ():
    return couleur[random.randint(0,len(couleur)-1)]

def changeCouleur ():
    canva.configure(bg=coul())

def cercle ():
    x = input("origine x du cercle")
    y = input("origine y du cercle")
    diametre = input("rayon")
    canva.create_oval(x,y,x+diametre,y+diametre)
root = tk.Tk(className="dessin")

canva = tk.Canvas(root,background=coul())
buttonCouleur = tk.Button(root, text="Changer couleur",command=changeCouleur)
buttonCerle = tk.Button(root, text="cercle",command=cercle)

canva.grid(row=1,column=1)
buttonCouleur.grid(row=0,column=1)
buttonCerle.grid(row=1,column=0)

root.mainloop()