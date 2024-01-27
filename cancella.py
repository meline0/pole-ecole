import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import csv
import sqlite3




fin = Tk()
connexion = sqlite3.connect('pole_ecole.db')
c = connexion.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS sauvegarde (
    id_client INTEGER,
	nom_ecole TEXT,
	lien TEXT,
	adresse TEXT,
	PRIMARY KEY (id_client, nom_ecole),
	FOREIGN KEY (id_client) REFERENCES client (id_client),
	FOREIGN KEY (nom_ecole) REFERENCES ecoles (nom_ecole)
    );
    """)
c.execute("""INSERT INTO sauvegarde 
VALUES ('Bob','es','fg','eee'),
       ('Charles', 'ee', 'eee','eee');""")




tv = ttk.Treeview(fin,
                      columns=("Ecole", "Adresse", "URL"),
                      show='headings')

    ###Les colonnes qu'il y a sur le tkinter
tv.column('#0')
tv.column('#1')
tv.column('#2')
tv.column('#3')

tv.heading('#0')
tv.heading('#1', text="Ecole")
tv.heading('#2', text="Adresse")
tv.heading('#3', text="URL")

def cancella(ecole):
        selezione = tv.selection()[0]
        mb_canc = messagebox.askokcancel(
            title="Confirmer la suppression",
            message="Voulez-vous confirmer l'élimination?")
        if mb_canc == True:
            tv.delete(selezione)
            fichier = open("mail.txt","r") 
            mail = fichier.read()
            c.execute("SELECT id_client FROM client WHERE mail ="+mail)
            id = c.fetchall()
            c.execute("DELETE FROM sauvegarde WHERE nom_ecole ='"+ecole+"'AND id_client = "+id)



tv.pack()

    ###Recupère les données de sauvegarde et les mets dans la page tkinter
c.execute("SELECT nom_ecole,lien,adresse FROM sauvegarde")
favoris = c.fetchall()
long = len(favoris)
for i in favoris:
    eco = i[0]
    url = i[1]
    adr = i[2]
    
    
    tv.insert("", 0, values=(adr, eco, url))

    #Met le bouton qui supprime renvoie a la fonction cancella
    puls_canc = Button(fin, text="Supprimer",
                       command=cancella(eco))
    puls_canc.pack()
