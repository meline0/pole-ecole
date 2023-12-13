import sqlite3

#Connexion
connexion = sqlite3.connect('pole_ecole.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL

#Création de la table
c.execute("""
    CREATE TABLE IF NOT EXISTS ecoles (
    id_ecole INTEGER PRIMARY KEY,
    nom_ecole TEXT,
    lien TEXT,
    description TEXT,
    adresse TEXT
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
    id_job INTEGER PRIMARY KEY,
    nom_job TEXT,
    description TEXT,
    formation TEXT
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS domaines (
    id_domaine INTEGER PRIMARY KEY,
    nom_domaine TEXT
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS proposer (
    id_domaine INTEGER,
	id_ecole INTEGER,
	PRIMARY KEY (id_domaine, id_ecole),
	FOREIGN KEY (id_domaine) REFERENCES domaines (id_domaine),
	FOREIGN KEY (id_ecole) REFERENCES ecoles (id_ecole) 
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS client (
    id_client INTEGER PRIMARY KEY,
	nom TEXT,
	prenom TEXT,
	mail TEXT,
	num INTEGER,
	date_naissance date,
	id_ecole INTEGER,
	id_job INTEGER,
	FOREIGN KEY (id_job) REFERENCES jobs (id_job),
	FOREIGN KEY (id_ecole) REFERENCES ecoles (id_ecole) 
    );
    """)

# ---- fin des instructions SQL

#Tkinter: fenêtre

fenetre = Tk()
fenetre.mainloop()

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

#Fin Tkinter

#Validation
connexion.commit()


#Déconnexion
connexion.close()
