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
	date_naissance date,
	id_ecole INTEGER,
	id_job INTEGER,
	FOREIGN KEY (id_job) REFERENCES jobs (id_job),
	FOREIGN KEY (id_ecole) REFERENCES ecoles (id_ecole) 
    );
    """)

#CSV
with open('mon_fichier.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    
    for row in reader:
        c.execute('''INSERT INTO bulletin VALUES (?,?,?)''', row)

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
