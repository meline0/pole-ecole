from tkinter import *
import webbrowser


def ouvrir_lien(url):
    webbrowser.open(url)

def ecoles():
    fenetre = Tk()
    fenetre.title("Pôle école")
    fenetre.geometry("900x670")
    fenetre.configure(bg='#9c742f')

    label = Label(fenetre, text="Les domaines de formations et leurs écoles",font=("arial", 25),fg="white")
    label.config(bg="#9c742f")
    label.pack()

    domaine1 = Label(text = "Agriculture", font=("arail", 18), fg = "black")
    domaine1.config(bg="#9c742f")
    domaine1.pack()

    ecole1 = Label(text="AgroParisTech \n 16 rue Claude Bernard, 75231 Paris Cedex 05 ",font=("arial", 9),fg="black")
    ecole1.config(bg="#9c742f")
    ecole1.pack()

    def ouvrir_lien_ecole1(event):
        ouvrir_lien("https://www.agroparistech.fr/")

    ecole1.bind("<Button-1>", ouvrir_lien_ecole1)

    ecole2 = Label(text="Institut National Polytechnique de Toulouse (INP-ENSAT) \n Avenue de l'Agrobiopôle, BP 32607 Auzeville Tolosane, 31326 Castanet Tolosan Cedex  ",font=("arial", 9),fg="black")
    ecole2.config(bg="#9c742f")
    ecole2.pack()

    def ouvrir_lien_ecole2(event):
        ouvrir_lien("https://www.inp-toulouse.fr/fr/index.html")

    ecole2.bind("<Button-2>", ouvrir_lien_ecole2)

    fenetre.mainloop()
ecoles()