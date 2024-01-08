import sqlite3
import tkinter as tk
import csv

#Connexion
connexion = sqlite3.connect('pole_ecole.db')

#Récupération d'un curseur
c = connexion.cursor()

# ------------------------------------------- début SQL ----------------------------------------#

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
	age INTEGER
    );
    """)

c.execute("""
    CREATE TABLE IF NOT EXISTS sauvegarde_e (
    id_client INTEGER PRIMARY KEY,
	ecole1 INTEGER,
	ecole2 INTEGER,
	ecole3 INTEGER,
	ecole4 INTEGER,
	ecole5 INTEGER,
	ecole6 INTEGER,
	ecole7 INTEGER,
	ecole8 INTEGER,
	ecole9 INTEGER,
	ecole10 INTEGER,
	FOREIGN KEY (id_client) REFERENCES client (id_client),
	FOREIGN KEY (ecole1) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole2) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole3) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole4) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole5) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole6) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole7) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole8) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole9) REFERENCES ecoles (id_ecole),
	FOREIGN KEY (ecole10) REFERENCES ecoles (id_ecole)
    );
    """)

#CSV

#Table école
with open('ecoles.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        c.execute('''INSERT INTO ecoles VALUES (?,?,?,?,?)''', row)

#Table jobs
with open('jobs.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        c.execute('''INSERT INTO jobs VALUES (?,?,?,?)''', row)

#Table domaines
with open('domaines.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        c.execute('''INSERT INTO domaines VALUES (?,?)''', row)

#Table proposer
with open('proposer.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        c.execute('''INSERT INTO proposer VALUES (?,?)''', row)

#Table client
def client():
    nom = input('Nom ? ')
    prenom = input('Prénom ? ')
    mail = input('Mail ? ')
    num = input('Numéro de téléphone ? ')
    age = input('Age ?')
    p = "INSERT INTO client VALUES ('" + nom + "','" + prenom + "','" + mail + "','" + num + "','" + age + "')"
    c.executescript(p)


#Rechercher

def afficher_domaines():
    #bouton pour afficher tous les domaines
    c.execute("SELECT nom_domaine FROM domaines")
    print(c.fetchall())

def rechercher_domaine():
    data = input('Formation' ) #bouton d'une formation spécifique
    c.execute("SELECT ecoles.nom_ecole FROM proposer JOIN ecoles ON         proposer.id_ecole = ecoles.id_ecole JOIN proposer.id_domaine = domaines.id_domaine WHERE nom_domaine = ?", "'" + data + "'")
    print(c.fetchall())

def rechercher_ecole():
    data = input('Ecole' ) #bouton d'une école spécifique
    c.execute("SELECT nom_ecole, lien, adresse, description FROM ecoles WHERE nom_ecole= ?", "'" + data + "'")
    print(c.fetchall())

#fin CSV

# ---------------------------------------------- fin SQL --------------------------------------------#

# ------------------------------------------- début Tkinter -----------------------------------------#

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Pôle école")

# Définir la taille de la fenêtre
window_width = 400
window_height = 300
center_window(root, window_width, window_height)

# Cadre 1
frame1 = tk.Frame(root, bg="lightblue", width=200, height=200)
frame1.pack_propagate(False)
frame1.pack(side=tk.LEFT, padx=10)

label1 = tk.Label(frame1, text="Cadre 1", font=("Helvetica", 14), bg="lightblue")
label1.pack(fill=tk.BOTH, expand=True)

# Cadre 2
frame2 = tk.Frame(root, bg="lightgreen", width=200, height=200)
frame2.pack_propagate(False)
frame2.pack(side=tk.RIGHT, padx=10)

label2 = tk.Label(frame2, text="Cadre 2", font=("Helvetica", 14), bg="lightgreen")
label2.pack(fill=tk.BOTH, expand=True)

# Lancement de la boucle principale
root.mainloop()

# -------------------------------------------- fin Tkinter ---------------------------------------------#

#Validation
connexion.commit()


#Déconnexion
connexion.close()
