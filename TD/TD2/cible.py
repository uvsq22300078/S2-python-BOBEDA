import tkinter as tk

root = tk.Tk(className="cercle")
canvas_size = 600

nb_cercle = 30
epaisseur = (canvas_size // 2 ) // nb_cercle
canva = tk.Canvas()
couleur = ["blue","green","black","yellow","magenta","red"]
canva = tk.Canvas(root,width= 600,height=600,bg="black")
for i in range (nb_cercle,0,-1):
    canva.create_oval(canvas_size/2+i*epaisseur,
                      canvas_size/2+i*epaisseur,
                      canvas_size/2-i*epaisseur,
                      canvas_size/2-i*epaisseur,
                      fill=couleur[-i%len(couleur)])
canva.grid(row=1,column=1)

root.mainloop()