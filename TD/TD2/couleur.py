import tkinter as tk
import random

root = tk.Tk(className="couleur")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_Rectangle (i,j,color):
    canva.create_rectangle(i,j,i+1,j+1,width=0,fill=color)

def Aleatoire ():
    for i in range (256):
        for j in range(256):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            couleur1 = get_color(r,g,b)
            draw_Rectangle(i,j,couleur1)

def degradeGris ():
    return None

def Degrade2d ():
    return None

canva = tk.Canvas(root,width= 256,height=256,highlightthickness=3,highlightbackground="ivory4",bg="black")
buttonAleatoire = tk.Button(root, text="Aleatoire",command=Aleatoire,foreground="blue")
buttonGris = tk.Button(root, text="degradeGris",command= degradeGris,foreground="blue")
button2D = tk.Button(root, text="Degrade2d",command=Degrade2d,foreground="blue")

canva.grid(row=1,column=1,rowspan=3)
buttonAleatoire.grid(row=1,column=0)
buttonGris.grid(row =2, column=0)
button2D.grid(row=3,column=0)
root.mainloop()