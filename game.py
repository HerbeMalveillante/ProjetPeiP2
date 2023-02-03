import tkinter as tk
import main


class Game(tk.Tk):


    def __init__(self,n, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Jeu de NIM")

        self.n = n
        self.grid = main.Grille(n=self.n, value="1"*self.n**2)
        self.canvas = tk.Canvas(bd=0, height=640, width=900, cursor="hand2")
        self.canvas.pack()

        self.updateDisplay()


    def updateDisplay(self):

        self.canvas.create_rectangle(0, 0, 900, 640, fill="beige") # fond
        self.canvas.create_rectangle(20, 20, 620, 620, fill="white") # plateau

        case = 600 // self.n
        # affichage des différentes cases
        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(20 + i*case, 20 + j*case, 20 + (i+1)*case, 20 + (j+1)*case, fill="AntiqueWhite4" if (i+j)%2==0  else "AntiqueWhite3")
                # si la valeur de la case correspondante est 1, on affiche une croix
                if self.grid.value[i*self.n + j] == "1":
                    self.canvas.create_line(20 + i*case + 10, 20 + j*case + 10, 20 + (i+1)*case - 10, 20 + (j+1)*case - 10, width=5, fill="black")
                    self.canvas.create_line(20 + i*case + 10, 20 + (j+1)*case - 10, 20 + (i+1)*case - 10, 20 + j*case + 10, width=5, fill="black")

        # affichage du bouton "valider" en bas à droite de l'écran
        bouton = self.canvas.create_rectangle(650, 550, 880, 620, fill="olive")
        # affichage du texte
        self.canvas.create_text(765, 585, text="Valider", font="Arial 20 bold", fill="white")
        # quand la souris survole le bouton, on change sa couleur pour la rendre plus visible
        self.canvas.tag_bind(bouton, "<Enter>", lambda event, color="green": self.canvas.itemconfig(bouton, fill=color))
        # quand la souris quitte le bouton, on change sa couleur pour la rendre plus visible
        self.canvas.tag_bind(bouton, "<Leave>", lambda event, color="olive": self.canvas.itemconfig(bouton, fill=color))

g = Game(3)
g.mainloop()
