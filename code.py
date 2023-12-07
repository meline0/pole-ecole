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

#Validation
connexion.commit()


#Déconnexion
connexion.close()
