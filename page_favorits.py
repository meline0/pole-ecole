from tkinter import *
import csv
import webbrowser

def favorits():
    fenetre_fav = Tk()
    fenetre_fav.title("Liste des favorits")
    fenetre_fav.geometry("900x670")
    fenetre_fav.configure(bg='#9c742f')

    text_fav = Text(fenetre_fav, wrap=WORD, bg='#9c742f', fg='white', font=("Arial", 12))
    text_fav.pack(expand=YES, fill=BOTH)
    text_fav.tag_configure("hyperlink", foreground="blue", underline=True)

    # Ouvrir le fichier CSV et lire son contenu
    with open('favorits.csv', 'r', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nom_ecole, adresse_ecole, url_site_ecole = row

            # Insérer le texte dans le widget Text
            text_fav.insert(END, f"\nNom de l'école: {nom_ecole}\n")
            text_fav.insert(END, f"Adresse: {adresse_ecole}\n")
            text_fav.insert(END, f"URL du site: {url_site_ecole}\n", "hyperlink")
            text_fav.insert(END, "\n" + "-" * 50 + "\n")

            # Associer une fonction pour ouvrir le lien dans le navigateur
            text_fav.tag_bind("hyperlink", "<Button-1>", lambda event, url=url_site_ecole: webbrowser.open_new(url))

favorits()
mainloop()
