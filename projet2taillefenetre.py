import tkinter as tk

class PageGarde(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pole Ecole")
        self.geometry = window.geometry(f"{ window.winfo_screenwidth()}x{window.winfo_screenheight()}+{x}+{y}")
        
        
        # Pages

        self.page_garde = FenetrePage(self, "Pole Ecole \n Trouve ton futur" )
        self.page_inscription = FenetrePage(self, "trouover moyen mettre truc sara  ")
        self.page_metiers = FenetrePage(self, " liste metiers") #les mettiers on les mets enn liste genre de boutons ou pas?
        self.page_ecoles = FenetrePage(self,"liste ecoles") #avec des boutons ?
        self.page_formations = FenetrePage(self, "liste formations du metier")
        self.page_favorits = FenetrePage(self, "liste favorits")

        
        self.page_actuelle = None  # Aucune page active au début
        self.afficher_page(self.page_garde) # Afficher la première page au démarrage
        self.page_actuelle = self.page_garde
        
        # Cadres
        
        frame_boutons = tk.Frame(self, bg = "darkgreen", width= 90, height = 400)
        frame_boutons.pack_propagate(False)
        frame_boutons.place(x=10, y=180)

        # Boutons 
        
        bouton_page_garde = tk.Button(self, text="Acceuil", command=lambda: self.afficher_page(self.page_garde) and self.page_actuelle.set(self.page_garde))
        bouton_page_garde.place(x= 15, y= 200)
        #bouton_page_garde.pack(side=tk.TOP)

        bouton_inscription = tk.Button(self, text="s'inscrire", command=lambda: self.afficher_page(self.page_inscription) and self.page_actuelle.set(self.page_inscription))
        bouton_inscription.place(x=620, y = 20)
        
        bouton_favorits = tk.Button(self, text="favorits", command=lambda: self.afficher_page(self.page_favorits) and self.page_actuelle.set(self.page_favorits))
        bouton_favorits.place(x=627, y = 50)

        bouton_metiers = tk.Button(self, text = "metiers", command=lambda: self.afficher_page(self.page_metiers) and self.page_actuelle.set(self.page_metiers))
        bouton_metiers.place(x = 20, y=230)

        bouton_ecoles = tk.Button(self, text="ecoles et formations",command=lambda: self.afficher_page(self.page_ecoles) and self.page_actuelle.set(self.page_ecoles))
        bouton_ecoles.place(x=20, y = 250)

        bouton_formations = tk.Button(self, text="formtions", command= lambda: self.afficher_page(self.page_formations) and self.page_actuelle.set(self.page_formations))
        bouton_formations.place(x=20, y = 270)
        
        
        
        
        
        
    def afficher_page(self, nouvelle_page):
        if self.page_actuelle:
            self.page_actuelle.pack_forget()  # Cacher la page active d'avant

        nouvelle_page.pack()  # Afficher le nouveau cadre
        self.page_actuelle = nouvelle_page  # Mettre à jour le cadre actif


    def afficher_boutons(self):
        if self.page_actuelle == self.page_inscription:
            bouton_inscription.pack_forget() 

class FenetrePage(tk.Frame):
    def __init__(self, fenetre, texte):
        super().__init__(fenetre)
        self.label = tk.Label(self, text=texte, font=("Helvetica", 14))
        self.label.pack(pady=50)

if __name__ == "__main__":
    app = PageGarde()
    app.mainloop()

