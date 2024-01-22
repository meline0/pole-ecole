from tkinter import *
import csv
import webbrowser

def favorits():

    fenetre_fav = Toplevel()
    fenetre_fav.title("Liste des favorits")
    fenetre_fav.geometry("900x670")
    fenetre_fav.configure(bg='#9c742f')

    
    text_fav = Text(fenetre_fav, wrap=WORD)
    text_fav.pack(expand=YES, fill=BOTH)
    text_fav.tag_configure("hyperlink", foreground="blue", underline=True)

    # overture du fichier CSV et lecture de son contenu
    with open('favorits.csv', 'r', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nom_ecole, adresse_ecole, url_site_ecole = row

           
            text_fav.insert(END, f"Nom de l'école: {nom_ecole}\n")
            text_fav.insert(END, f"Adresse: {adresse_ecole}\n")
            text_fav.insert(END, f"URL du site: {url_site_ecole}\n", "hyperlink")
            text_fav.tag_bind("hyperlink", "<Button-1>", lambda event, url=url_site_ecole: webbrowser.open_new(url)) # pour que le lien s'ouvre

favorits()
mainloop()