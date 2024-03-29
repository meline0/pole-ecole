import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import csv


fin = Tk()

def refresh_window():
    fin.update()
    fin.update_idletasks()

###Le fonction qui permet de supprimer une ligne
def cancella(ecole):
    fichier = open("mail.txt","r")
    mail = fichier.read()
    c.execute("SELECT id_client FROM client WHERE mail ="+mail)
    id = c.fetchall
    c.execute("DELETE FROM sauvegarde WHERE nom_ecole ='"+ecole+"'AND id_client = "+id)
    refresh_window()

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

tv.pack()

###Recupère les données de sauvegarde et les mets dans la page tkinter
c.execute("SELECT nom_ecole,lien,adresse FROM sauvegarde)
favoris = c.fetchall
for i in range(len(favoris)):
    eco = favoris[i][0]
    url = favoris[i][1]
    adr = favoris[i][2]
    

"""with open('favorits.csv', 'r+') as elenco:
    lettore = csv.reader(elenco)
    for row in lettore:
        adr = row[0]
        eco = row[1]
        url = row[2]"""
    
        tv.insert("", 0, values=(adr, eco, url))

#Met le bouton qui supprime renvoie a la fonction cancella
puls_canc = Button(fin, text="Supprimer",
                   command=cancella(eco))
puls_canc.pack()


fin.mainloop()
