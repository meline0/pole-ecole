from tkinter import *
from tkinter import ttk, messagebox
import webbrowser
import sqlite3


fenetre = Tk()
fenetre.geometry("400x200")

content_frame = None
fav_csv = "favorits.csv"

connexion = sqlite3.connect('pole_ecole.db')
c = connexion.cursor()

# ------------------------------------------- début SQL ----------------------------------------#

#Création de la table

c.execute("""
    CREATE TABLE IF NOT EXISTS ecoles (
    id_ecole INTEGER PRIMARY KEY,
    nom_ecole TEXT,
    lien TEXT,
    adresse TEXT
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
    id_job INTEGER PRIMARY KEY,
    nom_job TEXT,
    description TEXT
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
	num TEXT,
	age INTEGER,
	motdepasse TEXT
    );
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS sauvegarde (
    id_client INTEGER,
	nom_ecole TEXT,
	lien TEXT,
	adresse TEXT,
	PRIMARY KEY (id_client, nom_ecole)
	FOREIGN KEY (id_client) REFERENCES client (id_client),
	FOREIGN KEY (nom_ecole) REFERENCES ecoles (nom_ecole)
    );
    """)

#CSV
# #Table école
# with open('ecoles.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#
#     for row in reader:
#         c.execute('''INSERT INTO ecoles VALUES (?,?,?,?)''', row)
#
# #Table jobs
# with open('jobs.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#
#     for row in reader:
#         c.execute('''INSERT INTO jobs VALUES (?,?,?)''', row)
#
# #Table domaines
# with open('domaines.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#
#     for row in reader:
#         c.execute('''INSERT INTO domaines VALUES (?,?)''', row)
#
# #Table proposer
# with open('proposer.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#
#     for row in reader:
#         c.execute('''INSERT INTO proposer VALUES (?,?)''', row)
#
# #Table client
# c.execute('''INSERT INTO client VALUES (0, "test", "test", "test", 0, 0, "test")''')


#fin CSV

# ---------------------------------------------- fin SQL --------------------------------------------#


def inscription():
    label = Label(fenetre, text="Inscription")
    l1 = Label(fenetre, text = "Prénom:")
    l2 = Label(fenetre, text = "Nom:")
    l3 = Label(fenetre, text = "Age:")
    s = Spinbox(fenetre, from_=0, to=99)
    l4 = Label(fenetre, text = "Mail:")
    l5 = Label(fenetre, text = "Numéro de téléphone:")
    l6 = Label(fenetre, text = "Mot de passe:")


    label.grid(row = 0, column = 1, sticky = W, pady = 4)
    l1.grid(row = 1, column = 0, sticky = W, pady = 2)
    l2.grid(row = 2, column = 0, sticky = W, pady = 2)
    l3.grid(row = 3, column = 0, sticky = W, pady = 2)
    s.grid(row = 3, column = 1, sticky = W, pady = 2)
    l4.grid(row = 4, column = 0, sticky = W, pady = 2)
    l5.grid(row = 5, column = 0, sticky = W, pady = 2)
    l6.grid(row = 6, column = 0, sticky = W, pady = 2)

    def show_msg_enregistrer():
        c.execute("SELECT id_client FROM client")
        L=c.fetchall()
        id = str(L[-1][0]+1)
        h1 = str(getEntry(e1))
        h2 = str(getEntry(e2))
        h3 = str(getEntry(s))
        h4 = str(getEntry(e4))
        h5 = str(getEntry(e5))
        h6 = str(getEntry(e6))
        fichier = open("mail.txt", "w")
        fichier.write(h4)
        fichier.close()
        fenetre.destroy()
        p = "INSERT INTO client VALUES ('" + id + "','" + h2 + "','" + h1 + "','" + h4 + "','" + h5 + "','" + h3 + "','" + h6 + "')"
        c.executescript(p)

    def getEntry(nm):
        res = nm.get()
        return res

    button = ttk.Button(text= "Enregistrer>>",command=show_msg_enregistrer)
    button.grid(row = 6, column = 2, pady = 2)


    e1 = Entry(fenetre)
    e2 = Entry(fenetre)
    e4 = Entry(fenetre)
    e5 = Entry(fenetre)
    e6 = Entry(fenetre)

    e1.grid(row = 1, column = 1, pady = 2)
    e2.grid(row = 2, column = 1, pady = 2)
    e4.grid(row = 4, column = 1, pady = 2)
    e5.grid(row = 5, column = 1, pady = 2)
    e6.grid(row = 6, column = 1, pady = 2)


def connecter():
    label = Label(fenetre, text="Connexion")
    l1 = Label(fenetre, text = "Mail:")
    l2 = Label(fenetre, text = "Mot de passe:")

    label.grid(row = 0, column = 1, sticky = W, pady = 4)
    l1.grid(row = 1, column = 0, sticky = W, pady = 2)
    l2.grid(row = 2, column = 0, sticky = W, pady = 2)

    def show():
        h1 = str(getentry(e1))
        h2 = str(getentry(e2))
        fichier = open("mail.txt", "w")
        fichier.write(h1)
        fichier.close()
        fenetre.destroy()
        c.execute('''SELECT mail, motdepasse FROM client''')
        liste=c.fetchall()
        if (h1,h2) in liste:
            i=0
            #accéder au site
        else:
            #proposer de s'inscrire
            i=0


    def getentry(nm):
        res = nm.get()
        return res

    button = ttk.Button(text= "Se connecter>>",command=show)
    button.grid(row = 6, column = 2, pady = 2)

    e1 = Entry(fenetre)
    e2 = Entry(fenetre)

    e1.grid(row = 1, column = 1, pady = 2)
    e2.grid(row = 2, column = 1, pady = 2)



def window():
    #sign up
    button2 = ttk.Button(text= "S'inscrire",command=inscription)
    button2.grid(row = 2, column = 2, pady = 2)

    #sign in
    button3 = ttk.Button(text= "Se connecter",command=connecter)
    button3.grid(row = 3, column = 2, pady = 2)

    fenetre.mainloop()

    # def destroy():
    #     Button.destroy(button2)
    #     Button.destroy(button3)


window()

#Validation
connexion.commit()
#Déconnexion
connexion.close()


#Définir en tant que variable global les fenetres dans le programme principal
global zone1, zone2

# DEFINITIONS DES FONCTIONS
def metiers():
    #Définir en tant que variable global les fenetres dans chaque fonctions pour pouvoir travailler dessus
    global zone2,zone1

    fenetre = Tk()
    fenetre.title("Pôle école")
    fenetre.geometry("900x670")
    fenetre.configure(bg='#9c742f')

    label = Label(fenetre, text="Les Métiers",font=("arial", 25),fg="white")
    label.config(bg="#9c742f")
    label.pack()

    zone1=Frame(fenetre, bg='#9c742f')
    zone2=Frame(fenetre, bg='#9c752f')

    label1 = Label(zone1, text="Serveur/Serveuse",font=("arial", 10),fg="white")
    label1.config(bg="#9c742f")
    label1.pack()
    label2 = Label(zone1, text="Travailler dans un restaurant ou un café.",font=("arial", 9),fg="black")
    label2.config(bg="#9c742f")
    label2.pack()

    label3 = Label(zone1, text="Barista",font=("arial", 10),fg="white")
    label3.config(bg="#9c742f")
    label3.pack()
    label4 = Label(zone1, text="Préparer et servir des boissons dans un café.",font=("arial", 9),fg="black")
    label4.config(bg="#9c742f")
    label4.pack()

    label5 = Label(zone1, text="Caissier(ère)",font=("arial", 10),fg="white")
    label5.config(bg="#9c742f")
    label5.pack()
    label6 = Label(zone1, text="Travailler dans un magasin ou une supérette.",font=("arial", 9),fg="black")
    label6.config(bg="#9c742f")
    label6.pack()

    label7 = Label(zone1, text="Baby-sitting",font=("arial", 10),fg="white")
    label7.config(bg="#9c742f")
    label7.pack()
    label8 = Label(zone1, text="Garder des enfants pendant que les parents sont absents.",font=("arial", 9),fg="black")
    label8.config(bg="#9c742f")
    label8.pack()

    label9 = Label(zone1, text="Tuteur privé",font=("arial", 10),fg="white")
    label9.config(bg="#9c742f")
    label9.pack()
    label10 = Label(zone1, text="Aider d'autres étudiants à comprendre des matières spécifiques.",font=("arial", 9),fg="black")
    label10.config(bg="#9c742f")
    label10.pack()

    label11 = Label(zone1, text="Employé(e) de bibliothèque",font=("arial", 10),fg="white")
    label11.config(bg="#9c742f")
    label11.pack()
    label12 = Label(zone1, text="Travailler dans la bibliothèque de l'université.",font=("arial", 9),fg="black")
    label12.config(bg="#9c742f")
    label12.pack()

    label13 = Label(zone1, text="Assistant(e) de recherche",font=("arial", 10),fg="white")
    label13.config(bg="#9c742f")
    label13.pack()
    label14 = Label(zone1, text="Travailler avec des professeurs sur des projets de recherche.",font=("arial", 9),fg="black")
    label14.config(bg="#9c742f")
    label14.pack()

    label15 = Label(zone1, text="Assistant(e) de recherche",font=("arial", 10),fg="white")
    label15.config(bg="#9c742f")
    label15.pack()
    label16 = Label(zone1, text="Travailler avec des professeurs sur des projets de recherche.",font=("arial", 9),fg="black")
    label16.config(bg="#9c742f")
    label16.pack()

    label17 = Label(zone1, text="Vendeur(euse) en magasin",font=("arial", 10),fg="white")
    label17.config(bg="#9c742f")
    label17.pack()
    label18 = Label(zone1, text="Travailler dans le secteur de la vente au détail.",font=("arial", 9),fg="black")
    label18.config(bg="#9c742f")
    label18.pack()

    label19 = Label(zone1, text="Réceptionniste",font=("arial", 10),fg="white")
    label19.config(bg="#9c742f")
    label19.pack()
    label20 = Label(zone1, text="Travailler à la réception d'un hôtel ou d'un bureau.",font=("arial", 9),fg="black")
    label20.config(bg="#9c742f")
    label20.pack()

    label21 = Label(zone1, text="Garde de nuit",font=("arial", 10),fg="white")
    label21.config(bg="#9c742f")
    label21.pack()
    label22 = Label(zone1, text="Surveiller les résidences étudiantes ou travailler dans la sécurité.",font=("arial", 9),fg="black")
    label22.config(bg="#9c742f")
    label22.pack()

    label23 = Label(zone1, text="Agent(e) de call center",font=("arial", 10),fg="white")
    label23.config(bg="#9c742f")
    label23.pack()
    label24 = Label(zone1, text="Répondre aux appels téléphoniques pour une entreprise.",font=("arial", 9),fg="black")
    label24.config(bg="#9c742f")
    label24.pack()

    label25 = Label(zone1, text="Livreur(se)",font=("arial", 10),fg="white")
    label25.config(bg="#9c742f")
    label25.pack()
    label26 = Label(zone1, text="Livrer des repas, des colis ou des courses à domicile.",font=("arial", 9),fg="black")
    label26.config(bg="#9c742f")
    label26.pack()

    label27 = Label(zone2, text="Agent(e) d'accueil",font=("arial", 10),fg="white")
    label27.config(bg="#9c742f")
    label27.pack()
    label28 = Label(zone2, text="Travailler lors d'événements, de conférences ou de salons.",font=("arial", 9),fg="black")
    label28.config(bg="#9c742f")
    label28.pack()

    label29 = Label(zone2, text="Agent(e) de promotion",font=("arial", 10),fg="white")
    label29.config(bg="#9c742f")
    label29.pack()
    label30 = Label(zone2, text="Distribuer des échantillons ou des flyers pour promouvoir des produits.",font=("arial", 9),fg="black")
    label30.config(bg="#9c742f")
    label30.pack()

    label31 = Label(zone2, text="Photographe freelance",font=("arial", 10),fg="white")
    label31.config(bg="#9c742f")
    label31.pack()
    label32 = Label(zone2, text="Couvrir des événements, des mariages ou proposer des séances photo.",font=("arial", 9),fg="black")
    label32.config(bg="#9c742f")
    label32.pack()

    label33 = Label(zone2, text="Assistant(e) de vente en ligne",font=("arial", 10),fg="white")
    label33.config(bg="#9c742f")
    label33.pack()
    label34 = Label(zone2, text="Gérer les ventes et le service client pour des entreprises en ligne.",font=("arial", 9),fg="black")
    label34.config(bg="#9c742f")
    label34.pack()

    label35 = Label(zone2, text="Animateur(ice)",font=("arial", 10),fg="white")
    label35.config(bg="#9c742f")
    label35.pack()
    label36 = Label(zone2, text="Travailler dans des centres de loisirs ou des camps.",font=("arial", 9),fg="black")
    label36.config(bg="#9c742f")
    label36.pack()

    label37 = Label(zone2, text="Assistant(e) personnel(le)",font=("arial", 10),fg="white")
    label37.config(bg="#9c742f")
    label37.pack()
    label38 = Label(zone2, text="Aider des particuliers dans leurs tâches quotidiennes.",font=("arial", 9),fg="black")
    label38.config(bg="#9c742f")
    label38.pack()

    label39 = Label(zone2, text="Cours particuliers en ligne",font=("arial", 10),fg="white")
    label39.config(bg="#9c742f")
    label39.pack()
    label40 = Label(zone2, text="Enseigner des matières spécifiques à d'autres étudiants via des plateformes en ligne.",font=("arial", 9),fg="black")
    label40.config(bg="#9c742f")
    label40.pack()

    label41 = Label(zone2, text="Testeur(euse) de produits",font=("arial", 10),fg="white")
    label41.config(bg="#9c742f")
    label41.pack()
    label42 = Label(zone2, text="Tester des produits pour des entreprises.",font=("arial", 9),fg="black")
    label42.config(bg="#9c742f")
    label42.pack()

    label43 = Label(zone2, text="Agent(e) de sondage",font=("arial", 10),fg="white")
    label43.config(bg="#9c742f")
    label43.pack()
    label44 = Label(zone2, text="Réaliser des sondages ou des enquêtes pour des instituts de recherche.",font=("arial", 9),fg="black")
    label44.config(bg="#9c742f")
    label44.pack()

    label45 = Label(zone2, text="Assistant(e) en événementiel",font=("arial", 10),fg="white")
    label45.config(bg="#9c742f")
    label45.pack()
    label46 = Label(zone2, text="Travailler sur l'organisation d'événements.",font=("arial", 9),fg="black")
    label46.config(bg="#9c742f")
    label46.pack()

    label47 = Label(zone2, text="Assistant(e) en marketing digital",font=("arial", 10),fg="white")
    label47.config(bg="#9c742f")
    label47.pack()
    label48 = Label(zone2, text="Aider à gérer les médias sociaux, la publicité en ligne, etc.",font=("arial", 9),fg="black")
    label48.config(bg="#9c742f")
    label48.pack()

    label49 = Label(zone2, text="Assistant(e) en informatique",font=("arial", 10),fg="white")
    label49.config(bg="#9c742f")
    label49.pack()
    label50 = Label(zone2, text="Aider d'autres étudiants ou entreprises avec des problèmes informatiques.",font=("arial", 9),fg="black")
    label50.config(bg="#9c742f")
    label50.pack()

    bouton_retour=Button(zone2, text=">>>retour",fg="white", command=fenetre.quit)
    bouton_retour.config(bg="#573f17")
    bouton_retour.pack(side='bottom')

    zone1.pack(fill=Y, padx=30,pady=60,side="left")
    zone2.pack(fill=Y, padx=30,pady=60,side="right")



    fenetre.mainloop()

def creer_label_ecole(parent, nom, adresse, url):
    label_nom = Label(parent, text=nom, font=("arial", 18), fg="black", bg="#9c742f")
    label_nom.pack()

    label_adresse = Label(parent, text=adresse, font=("arial", 9), fg="black", bg="#9c742f")
    label_adresse.pack()

    label_lien = Label(parent, text=url, font=("arial", 9), fg="blue", cursor="hand2", bg="#9c742f")
    label_lien.pack()

    def ouvrir_lien(event):
        webbrowser.open(url)

    label_lien.bind("<Button-1>", ouvrir_lien)

    checked = BooleanVar()
    checkup_button = Checkbutton(parent, text="Checkup", variable=checked, command=lambda: etat_bouton_fav(nom, adresse, url, fav_csv, checked.get()))
    checkup_button.pack()

def etat_bouton_fav(nom, adresse, url, csv_file, coche):
    if coche:
        enregistre_dans_fav(nom, url,adresse)
#    else:
#        enregistre_dans_fav(nom, adresse, url, csv_file, delete=True)

def enregistre_dans_fav(nom, lien, adresse):
    fichier = open("mail.txt", "r")
    mail = fichier.read()
    c.execute("SELECT id_client From client WHERE mail ="+mail)
    id = c.fetchall
    c.execute('''INSERT INTO sauvegarde VALUES (?,?,?,?)''', id, nom, lien, adresse)


#def centrer_fenetre(window, width, height):
#    screen_width = window.winfo_screenwidth()
#    screen_height = window.winfo_screenheight()#
#
#    x = (screen_width - width) // 2
#    y = (screen_height - height) // 2
#    window.geometry(f"{width}x{height}+{x}+{y}")

def ecoles():
    fenetre = Tk()
    fenetre.title("Pôle école")
    fenetre.geometry("900x670")
    fenetre.configure(bg='#9c742f')

    cadre_scroll = Frame(fenetre, bg="#9c742f")
    cadre_scroll.pack(fill="both", expand=True)
    scrollbar = Scrollbar(cadre_scroll, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    canvas = Canvas(cadre_scroll, yscrollcommand=scrollbar.set, bg="#9c742f")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    content_frame = Frame(canvas, bg="#9c742f")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    labelTitre = Label(content_frame, text="Les domaines de formations et leurs écoles", font=("arial", 25), fg="white", bg="#9c742f")
    labelTitre.pack()

    labelDom1 = Label(content_frame, text="\n\n Agriculture\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom1.pack()
    creer_label_ecole(content_frame, "AgroParisTech", "16 rue Claude Bernard, 75231 Paris Cedex 05", "https://www.agroparistech.fr/" "\n")
    creer_label_ecole(content_frame, "INP-ENSAT", "Avenue de l'Agrobiopôle, BP 32607 Auzeville Tolosane, 31326 Castanet Tolosan Cedex", "https://www.inp-toulouse.fr/fr/index.html""\n")
    creer_label_ecole(content_frame, "Agrocampus Ouest","65 Rue de Saint-Brieuc, CS 84215, 35042 Rennes Cedex", "https://www.institut-agro-rennes-angers.fr/""\n")
    creer_label_ecole(content_frame, "SupAgro Montpellier", "2 Place Viala, 34060 Montpellier Cedex 2", "https://www.supagro.fr/""\n")
    creer_label_ecole(content_frame, "Institut Agro La Rochelle", "1 cours des Dames, 17100 Saintes", "https://www.institut-agro.fr/fr""\n")
    creer_label_ecole(content_frame, "École d'Ingénieurs de Purpan", "75 Voie du TOEC, 31076 Toulouse Cedex 3", "https://www.purpan.fr/""\n")
    creer_label_ecole(content_frame, "UniLaSalle Beauvais", "19 Rue Pierre Waguet, BP 30313, 60026 Beauvais Cedex", "https://www.unilasalle.fr/""\n")
    creer_label_ecole(content_frame, "ISARA Lyon", "23 Rue Jean Baldassini, 69364 Lyon Cedex 07", "https://www.isara.fr/""\n")
    creer_label_ecole(content_frame, "ESA Angers", "55 Rue Rabelais, 49007 Angers Cedex 01", "https://www.groupe-esa.com/""\n")
    creer_label_ecole(content_frame, "ENSAIA Nancy", "2 avenue de la forêt de Haye, 54505 Vandoeuvre-lès-Nancy Cedex", "https://www.ensaia.univ-lorraine.fr/""\n")

    labelDom2 = Label(content_frame, text="\n\n Armée\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom2.pack()
    creer_label_ecole(content_frame, "École Spéciale Militaire de Saint-Cyr (ESM Saint-Cyr)", "56380 Guer", "https://www.terre.defense.gouv.fr/amscc/mieux-nous-connaitre/lacademie-militaire-saint-cyr-coetquidan/ecole-speciale-militaire""\n")
    creer_label_ecole(content_frame, "École de l'Air", "Chemin St Jean, 13300 Salon-de-Provence", "https://www.ecole-air-espace.fr/""\n")
    creer_label_ecole(content_frame, "École Navale", "BCRM BREST, Rue du Poulmic, 29160 Lanvéoc", "https://www.ecole-navale.fr/""\n")
    creer_label_ecole(content_frame, "École de Gendarmerie de Fontainebleau", "Rue de la Charité, 77210 Avon", "https://www.gendarmerie.interieur.gouv.fr/cegn/les-ecoles-de-gendarmerie/ecoles-des-sous-officiers/fontainebleau""\n")
    creer_label_ecole(content_frame, "École Militaire Interarmes (EMIA)", "Av. Maréchal Foch, 56380 Guer", "https://www.emia-57.fr/""\n")
    creer_label_ecole(content_frame, "École de Guerre", "1 Pl. de l'École Militaire, 75007 Paris", "https://ecoledeguerre.paris/""\n")
    creer_label_ecole(content_frame, "École de Santé des Armées (ESA)", "331 Av. Général de Gaulle, 69500 Bron", "https://www.emslb.defense.gouv.fr/""\n")
    creer_label_ecole(content_frame, "École Militaire de l'Infanterie (EMI)", "1580 Av. de la Grande Armée, 83300 Draguignan", "https://www.terre.defense.gouv.fr/emd/ecole-dinfanterie/formation-au-sein-lecole-dinfanterie""\n")
    creer_label_ecole(content_frame, "École des Applications Militaires de l'Énergie Atomique (EAMEA)", "1 rue du recteur Daure. CS 60040. 14006 Caen Cedex", "https://www.normandie-energies.com/membre/eamea-2/""\n")

    labelDom3 = Label(content_frame, text="\n\n Finaces\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom3.pack()
    creer_label_ecole(content_frame, "Master Banque et Finance - Université Paris-Dauphine", "Place du Maréchal de Lattre de Tassigny, 75775 Paris Cedex 16, France", "https://dauphine.psl.eu/formations/masters/finance/m2-banque-et-finance""\n")
    creer_label_ecole(content_frame, "Master in Finance - ESCP Business School", "79 Avenue de la République, 75011 Paris, France", "https://escp.eu/""\n")
    creer_label_ecole(content_frame, "Master Finance et Marché de l'Art - IAE Paris - Sorbonne Business School", "21 Rue Broca, 75005 Paris, France", "http://iae-paris.com/fr""\n")
    creer_label_ecole(content_frame, "MSc in Banking and Finance - EMLYON Business School", "23 Avenue Guy de Collongue, 69134 Écully Cedex, France", "https://em-lyon.com/""\n")
    creer_label_ecole(content_frame, "MSc International Finance - HEC Paris", "1 Rue de la Libération, 78350 Jouy-en-Josas, France", "https://www.hec.edu/fr""\n")
    creer_label_ecole(content_frame, "Master in Finance - INSEAD", "Boulevard de Constance, 77305 Fontainebleau Cedex, France", "https://www.insead.edu/""\n")
    creer_label_ecole(content_frame, "Master Droit et Ingénierie Financière - Université Panthéon-Assas", "12 Place du Panthéon, 75231 Paris Cedex 05, France", "https://www.u-paris2.fr/fr""\n")
    creer_label_ecole(content_frame, "MSc Corporate Financial Management - SKEMA Business School", "60 Rue Dostoïevski, 06560 Sophia Antipolis, France", "https://www.skema.edu/""\n")
    creer_label_ecole(content_frame, "Master Banque et Finance - Université Paris Nanterre", "200 Avenue de la République, 92001 Nanterre Cedex, France", "https://www.parisnanterre.fr/""\n")
    creer_label_ecole(content_frame, "MSc Finance - Grenoble Ecole de Management", "12 Rue Pierre Sémard, 38000 Grenoble, France", "https://www.grenoble-em.com/""\n")

    labelDom4 = Label(content_frame, text="\n\n Commerce\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom4.pack()
    creer_label_ecole(content_frame, "ESCP Business School", "79 Avenue de la République, 75011 Paris", "\nhttps://www.escp.eu/""\n")
    creer_label_ecole(content_frame, "HEC Paris", "1 Rue de la Libération, 78350 Jouy-en-Josas", "\nhttps://www.hec.edu/""\n")
    creer_label_ecole(content_frame, "EM Lyon Business School", "23 Avenue Guy de Collongue, 69134 Écully", "\nhttps://www.em-lyon.com/""\n")
    creer_label_ecole(content_frame, "EDHEC Business School", "24 Avenue Gustave Delory, 59100 Roubaix", "\nhttps://www.edhec.edu/""\n")
    creer_label_ecole(content_frame, "NEOMA Business School", "1 Rue du Maréchal Juin, 76130 Mont-Saint-Aignan", "\nhttps://www.neoma-bs.com/""\n")
    creer_label_ecole(content_frame, "Grenoble Ecole de Management", "12 Rue Pierre Sémard, 38000 Grenoble", "\nhttps://www.grenoble-em.com/""\n")
    creer_label_ecole(content_frame, "KEDGE Business School", "Domaine de Luminy, 13009 Marseille", "\nhttps://student.kedge.edu/""\n")
    creer_label_ecole(content_frame, "Audencia Business School", "8 Route de la Jonelière, 44312 Nantes", "\nhttps://www.audencia.com/""\n")
    creer_label_ecole(content_frame, "Toulouse Business School", "20 Boulevard Lascrosses, 31068 Toulouse", "\nhttps://www.tbs-education.fr/""\n")
    creer_label_ecole(content_frame, "ICN Business School", "3 Rue de l'Arsenal, 54000 Nancy", "\nhttps://www.icn-artem.com/""\n")

    labelDom5 = Label(content_frame, text="\n\n Architecture\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom5.pack()
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Architecture de Paris-Belleville (ENSAPB)", "60 Boulevard de la Villette, 75019 Paris, France", "\nhttps://www.paris-belleville.archi.fr/""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Architecture de Lyon (ENSAL)", "3 Rue Maurice Audin, 69120 Vaulx-en-Velin, France", "https://www.lyon.archi.fr/""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Architecture de Marseille (ENSAM)", "184 Avenue de Luminy, 13009 Marseille, France", "https://www.marseille.archi.fr/""\n")
    creer_label_ecole(content_frame, "École des Ponts ParisTech - Ingénieur du Corps des Ponts, des Eaux et des Forêts (ENPC)", "6-8 Avenue Blaise Pascal, Cité Descartes, 77455 Marne-la-Vallée Cedex 2, France", "https://ecoledesponts.fr/""\n")
    creer_label_ecole(content_frame, "Institut National des Sciences Appliquées de Strasbourg (INSA Strasbourg) - Génie Civil", "24 Boulevard de la Victoire, 67084 Strasbourg Cedex, France", "https://www.insa-strasbourg.fr/fr/genie-civil/""\n")
    creer_label_ecole(content_frame, "École Nationale des Travaux Publics de l'État (ENTPE)", "3 Rue Maurice Audin, 69120 Vaulx-en-Velin, France", "https://www.entpe.fr/""\n")
    creer_label_ecole(content_frame, "École Spéciale des Travaux Publics, du Bâtiment et de l'Industrie (ESTP Paris)", "28 Avenue du Président Wilson, 94234 Cachan Cedex, France", "https://www.estp.fr/""\n")
    creer_label_ecole(content_frame, "École d'Architecture de la Ville & des Territoires Paris-Est (EAVT)", "12 Avenue Blaise Pascal, 77420 Champs-sur-Marne, France", "https://paris-est.archi.fr/""\n")
    creer_label_ecole(content_frame, "École d'Architecture de Nantes (ENSA Nantes)", "6 Quai François Mitterrand, 44200 Nantes, France", "https://www.nantes.archi.fr/""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Architecture et de Paysage de Bordeaux (ENSAP Bordeaux)", "740 Cours de la Libération, 33405 Talence Cedex, France", "https://www.bordeaux.archi.fr/""\n")

    labelDom6 = Label(content_frame, text="\n\n Droit, politique\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom6.pack()
    creer_label_ecole(content_frame, "Université Panthéon-Assas - Centre Assas", "92 Rue d'Assas, 75006 Paris", "\nhttps://www.u-paris2.fr/fr/universite/linstitution/implantations/centre-assas""\n")
    creer_label_ecole(content_frame, "Sciences Po Paris", "27 Rue Saint-Guillaume, 75007 Paris", "\nhttps://www.sciencespo.fr/fr/""\n")
    creer_label_ecole(content_frame, "Université Paris 1 Panthéon-Sorbonne - UFR 09 - Droit et Science Politique", "12 Place du Panthéon, 75005 Paris", "\nhttps://formations.pantheonsorbonne.fr/fr/catalogue-des-formations/licence-L/licence-droit-KBT8CDAC/double-licence-droit-science-politique-KBT8LTQN.html""\n")
    creer_label_ecole(content_frame, "Université Paris 2 Panthéon-Assas - UFR Droit", "12 Rue de l'École de Médecine, 75006 Paris", "\nhttps://www.u-paris2.fr/fr/formations/offre-de-formation/formations-en-droit""\n")
    creer_label_ecole(content_frame, "Université Paris Nanterre - UFR SSA", "200 Avenue de la République, 92001 Nanterre Cedex", "\nhttps://ufr-ssa.parisnanterre.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - Faculté de Droit, Sciences politiques et Gestion", "1 Place d'Athènes, 67045 Strasbourg", "\nhttps://droit.unistra.fr/""\n")
    creer_label_ecole(content_frame, "Université Toulouse 1 Capitole - Faculté de Droit et Science Politique", "2 Rue du Doyen-Gabriel-Marty, 31042 Toulouse", "\nhttps://www.ut-capitole.fr/accueil/universite/composantes/faculte-de-droit-et-science-politique""\n")
    creer_label_ecole(content_frame, "Université Lyon 3 Jean Moulin - Faculté de Droit", "15 Quai Claude Bernard, 69007 Lyon", "\nhttps://facdedroit.univ-lyon3.fr/""\n")
    creer_label_ecole(content_frame, "Université Aix-Marseille - Faculté de Droit et de Science Politique", "3 Avenue Robert Schuman, 13628 Aix-en-Provence", "\nhttps://facdedroit.univ-amu.fr/""\n")
    creer_label_ecole(content_frame, "Université Lille - Faculté des Sciences Juridiques, Politiques et Sociales", "1 Place Déliot, 59000 Lille", "\nhttps://droit.univ-lille.fr/""\n")

    labelDom7 = Label(content_frame, text="\n\n Électronique, robotique\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom7.pack()
    creer_label_ecole(content_frame, "CentraleSupélec - Électricité, Électronique, Robotique", "3 Rue Joliot-Curie, 91192 Gif-sur-Yvette Cedex, France", "\nhttps://www.centralesupelec.fr/""\n")
    creer_label_ecole(content_frame, "ENSEA - École Nationale Supérieure de l'Électronique et de ses Applications", "6 Avenue du Ponceau, 95014 Cergy-Pontoise Cedex, France", "\nhttp://www.ensea.fr/""\n")
    creer_label_ecole(content_frame, "INSA Lyon - Génie Électrique", "20 Avenue Albert Einstein, 69621 Villeurbanne Cedex, France", "\nhttps://www.insa-lyon.fr/""\n")
    creer_label_ecole(content_frame, "École Polytechnique - Département d'Électronique", "Route de Saclay, 91128 Palaiseau Cedex, France", "\nhttps://www.polytechnique.edu/""\n")
    creer_label_ecole(content_frame, "SUPÉLEC - Électricité, Électronique, Automatique", "3 Rue Joliot-Curie, 91192 Gif-sur-Yvette Cedex, France", "\nhttps://www.centralesupelec.fr/fr/masters""\n")
    creer_label_ecole(content_frame, "INP Toulouse - ENSEEIHT - Génie Électrique", "2 Rue Charles Camichel, 31071 Toulouse Cedex 7, France", "\nhttps://www.inp-toulouse.fr/fr/index.html""\n")
    creer_label_ecole(content_frame, "Télécom Paris - Électronique et Communications Numériques", "19 Place Marguerite Perey, 91120 Palaiseau, France", "\nhttps://www.telecom-paris.fr/""\n")
    creer_label_ecole(content_frame, "ESIEE Paris - École d'Ingénieurs en Informatique, Électronique et Électrotechnique", "2 Boulevard Blaise Pascal, 93160 Noisy-le-Grand, France", "\nhttps://www.esiee.fr/""\n")
    creer_label_ecole(content_frame, "ENSEIRB-MATMECA - Électronique, Informatique, Télécommunications", "1 Avenue du Dr Albert Schweitzer, 33402 Talence Cedex, France", "\nhttps://enseirb-matmeca.bordeaux-inp.fr/""\n")
    creer_label_ecole(content_frame, "Arts et Métiers ParisTech - Énergie, Électricité, Automatique", "151 Boulevard de l'Hôpital, 75013 Paris, France", "\nhttps://www.artsetmetiers.fr/""\n")

    labelDom8 = Label(content_frame, text="\n\n Environnement\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom8.pack()
    creer_label_ecole(content_frame, "École Nationale des Ponts et Chaussées (ENPC)", "15 Rue de la Fontaine au Roi, 75011 Paris", "https://www.ecoledesponts.fr/""\n")
    creer_label_ecole(content_frame, "AgroParisTech", "16 Rue Claude Bernard, 75231 Paris Cedex 05", "https://www.agroparistech.fr/""\n")
    creer_label_ecole(content_frame, "MINES ParisTech", "60 Boulevard Saint-Michel, 75006 Paris", "https://www.mines-paristech.fr/""\n")
    creer_label_ecole(content_frame, "École des Ponts Business School", "6-8 Avenue Blaise Pascal, 77455 Marne-la-Vallée", "https://pontsbschool.com/""\n")
    creer_label_ecole(content_frame, "Institut National de l'Environnement Industriel et des Risques (INERIS)", "Parc Technologique ALATA, BP 2, 60550 Verneuil-en-Halatte", "http://www.ineris.fr/""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure de Chimie de Montpellier (ENSCM)", "8 Rue de l'École Normale, 34296 Montpellier Cedex 5", "https://www.enscm.fr/""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Architecture de Lyon (ENSAL)", "3 Rue Maurice Audin, 69120 Vaulx-en-Velin", "https://www.lyon.archi.fr/""\n")
    creer_label_ecole(content_frame, "École Supérieure d'Ingénieurs en Électrotechnique et Électronique (ESIEE) Paris", "2 Boulevard Blaise Pascal, Cité Descartes, 93160 Noisy-le-Grand", "https://www.esiee.fr/""\n")
    creer_label_ecole(content_frame, "Université de Technologie de Troyes (UTT) - Département Génie de l'Environnement", "12 Rue Marie Curie, CS 42060, 10004 Troyes Cedex", "https://www.utt.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - Faculté des Sciences de la Vie ", "23 Rue Becquerel, 67000 Strasbourg", "https://www.unistra.fr/""\n")

    labelDom9 = Label(content_frame, text="\n\n Managment\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom9.pack()
    creer_label_ecole(content_frame, "HEC Paris - Hautes Études Commerciales", "1 Rue de la Libération, 78350 Jouy-en-Josas, France", "https://www.hec.edu/""\n")
    creer_label_ecole(content_frame, "ESSEC Business School - École Supérieure des Sciences Économiques et Commerciales", "Avenue Bernard Hirsch, 95021 Cergy-Pontoise Cedex, France", "https://www.essec.edu/""\n")
    creer_label_ecole(content_frame, "EDHEC Business School", "24 Avenue Gustave Delory, 59100 Roubaix, France", "https://www.edhec.edu/""\n")
    creer_label_ecole(content_frame, "Audencia Business School", "8 Route de la Jonelière, 44312 Nantes Cedex 3, France", "https://www.audencia.com/""\n")
    creer_label_ecole(content_frame, "EM Lyon Business School", "23 Avenue Guy de Collongue, 69134 Écully Cedex, France", "https://www.em-lyon.com/""\n")
    creer_label_ecole(content_frame, "NEOMA Business School", "1 Rue du Maréchal Juin, 76130 Mont-Saint-Aignan, France", "https://www.neoma-bs.com/""\n")
    creer_label_ecole(content_frame, "Grenoble Ecole de Management", "12 Rue Pierre Sémard, 38000 Grenoble, France", "https://www.grenoble-em.com/""\n")
    creer_label_ecole(content_frame, "IAE Paris - Sorbonne Business School", "21 Rue Broca, 75005 Paris, France", "https://www.iae-paris.com/""\n")
    creer_label_ecole(content_frame, "Toulouse Business School", "20 Boulevard Lascrosses, 31068 Toulouse Cedex 7, France", "https://www.tbs-education.fr/""\n")
    creer_label_ecole(content_frame, "KEDGE Business School", "Domaine de Luminy, 13009 Marseille, France", "https://kedge.edu/""\n")

    labelDom10 = Label(content_frame, text="\n\n Histoire\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom10.pack()
    creer_label_ecole(content_frame, "Université Paris 1 Panthéon-Sorbonne", "12 Place du Panthéon, 75005 Paris", "https://www.pantheonsorbonne.fr/""\n")
    creer_label_ecole(content_frame, "Université Paris-Sorbonne", "1 Rue Victor Cousin, 75005 Paris", "https://lettres.sorbonne-universite.fr/faculte-des-lettres/ufr/ufr-histoire-de-l-art-et-archeologie""\n")
    creer_label_ecole(content_frame, "Université Lyon 3 Jean Moulin", "18 Rue Chevreul, 69007 Lyon", "https://www.univ-lyon3.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg", "22 Rue René Descartes, 67084 Strasbourg", "https://www.unistra.fr/""\n")
    creer_label_ecole(content_frame, "Université Paris Nanterre", "200 Avenue de la République, 92001 Nanterre Cedex", "https://www.parisnanterre.fr/""\n")
    creer_label_ecole(content_frame, "Université Aix-Marseille", "3 Place Victor Hugo, 13331 Marseille Cedex 03", "https://www.univ-amu.fr/""\n")
    creer_label_ecole(content_frame, "Université Toulouse 2 Jean Jaurès", "5 Allées Antonio Machado, 31058 Toulouse", "https://www.univ-tlse2.fr/""\n")
    creer_label_ecole(content_frame, "Université de Nantes", "Chemin de la Censive du Tertre, 44313 Nantes", "https://www.univ-nantes.fr/""\n")
    creer_label_ecole(content_frame, "Université de Lorraine", "23 Boulevard Albert 1er, 54000 Nancy", "https://www.univ-lorraine.fr/""\n")
    creer_label_ecole(content_frame, "Université de Bordeaux", "1 Allée Daguin, 33607 Pessac Cedex", "https://www.u-bordeaux.fr/""\n")

    labelDom11 = Label(content_frame, text="\n\n Hôtellerie-restauration\n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom11.pack()
    creer_label_ecole(content_frame, "Institut Paul Bocuse - École de Cuisine, de Pâtisserie et d'Hôtellerie", "Château du Vivier, Ecully, 69130 Ecully, France", "https://www.institutlyfe.com/?gad_source=1&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGcn7ssYJUN1IChUGp-uD9ZZcv5z4oapjnKHvx48VjnVGvX8Y6XfN2hoC-EsQAvD_BwE""\n")
    creer_label_ecole(content_frame, "Lycée Hôtelier de Toulouse", "20 Avenue Camille Pujol, 31500 Toulouse, France", "https://hotellerie-tourisme.mon-ent-occitanie.fr/""\n")
    #creer_label_ecole(content_frame, "FERRANDI Paris - École Supérieure de Cuisine et de Management Hôtelier", "28 Rue de l'Abbé Grégoire, 75006 Paris, France", "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwi_-sqC452DAxULimgJHRoxA6UYABABGgJ3Zg&ase=2&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGZMA5PMNs3ZC-nMeu0CLLP_wsW1_3e-4OF5823sQQ5JtXnmzkKzffRoCOiUQAvD_BwE&ohost=www.google.com&cid=CAESVuD21xHfTTVQZQeCKYqcifnYDcQOB_X0AiCGWNsbDGEw3sGpDoW5LintyYWfRLHxSz_cR2dvF7aDo5ZMDN0rUriwW5bB1IjpLjf_p0SfW_SUwXsmfMGB&sig=AOD64_2yCbPPXcFVvYrZMA3ZBF7wx5bV6Q&q&nis=4&adurl&ved=2ahUKEwjkpL-C452DAxX3_rsIHfLmCPMQ0Qx6BAgHEAE")
    creer_label_ecole(content_frame, "Vatel Bordeaux - International Business School Hotel & Tourism Management", "4 Cours du Médoc, 33300 Bordeaux, France", "https://www.vatel.fr/fr/ecole-hoteliere-bordeaux/presentation-vatel-bordeaux?utm_source=google_business&utm_medium=bordeaux""\n")
    #creer_label_ecole(content_frame, "Ecole Supérieure de Tourisme (EST) Paris", "38 Quai de Jemmapes, 75010 Paris, France", "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiRscne4p2DAxUqn2gJHQAiAe4YABABGgJ3Zg&ase=2&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGfb7UmPPXNw6x7cBOSPaJauePigwO5jhTtOE2RJmkshkgZtHG9buWhoCGagQAvD_BwE&ohost=www.google.com&cid=CAESVuD2pLnFbUdzM2LBvzCU_wu0PrJl11xBtVu6SKktvpShMb1KWFlqVsBYX_L6nMOTk49wLMY8rNDTwVJZHZbwvou9qUYPOGkw3yYeRTt4C6eSq-FoJkN0&sig=AOD64_3_OgLclJDC4qMbU8YEMcHg30H7_g&q&nis=4&adurl&ved=2ahUKEwjUvcDe4p2DAxUMhv0HHRQVAi4Q0Qx6BAgDEAE")
    creer_label_ecole(content_frame, "Institut Vatel Nîmes", "140 Rue Vatel, 30900 Nîmes, France", "https://www.vatel.fr/fr/ecole-hoteliere-nimes/presentation-vatel-nimes""\n")
    creer_label_ecole(content_frame, "Lycée Hôtelier Georges Baptiste de Canteleu", "64 Rue Pasteur, 76380 Canteleu, France", "https://georgesbaptiste.fr/""\n")
    creer_label_ecole(content_frame, "Lycée des Métiers de l'Hôtellerie et du Tourisme de Toulon", "35 Avenue Stalingrad, 83000 Toulon, France", "https://www.lyc-anne-sophie-pic.ac-nice.fr/""\n")
    creer_label_ecole(content_frame, "Lycée Hôtelier de Nice", "2 Avenue Cap de Croix, 06100 Nice, France", "https://www.lycee-paul-augier.com/""\n")

    labelDom12 = Label(content_frame, text="\n\n Audiovisuel \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom12.pack()
    creer_label_ecole(content_frame, "La Fémis", "6 Rue Francoeur, 75018 Paris", "https://www.femis.fr/""\n")
    creer_label_ecole(content_frame, "École nationale supérieure Louis-Lumière", "La Cité du Cinéma, 20 Rue Ampère, 93200 Saint-Denis", "https://www.ens-louis-lumiere.fr/""\n")
    creer_label_ecole(content_frame, "ESRA (École Supérieure de Réalisation Audiovisuelle)", "9 Quai des Deux Emmanuels, 06300 Nice", "https://esra.edu/""\n")
    creer_label_ecole(content_frame, "ISITV (Institut Supérieur d'Ingénieurs de la Ville de Paris)", "19 Rue Alfred de Vigny, 75008 Paris", "https://www.studyrama.com/formations/filieres/ecoles-d-ingenieurs/linstitut-des-sciences-de-lingenieur-de-toulon-et-du-var-isitv-forme-des-ingenieurs-dans-3-specialites-26540""\n")
    creer_label_ecole(content_frame, "EICAR (École Internationale de Création Audiovisuelle et de Réalisation)", "61 Rue du Landy, 93210 La Plaine-Saint-Denis", "https://www.eicar.fr/""\n")
    creer_label_ecole(content_frame, "CinéCréatis", "7 Quai Chateaubriand, 35000 Rennes", "http://www.cinecreatis.net""\n")
    creer_label_ecole(content_frame, "EMC (École des Métiers de la Communication)", "68 Avenue de la République, 75011 Paris", "https://www.emc.fr/""\n")
    creer_label_ecole(content_frame, "ECS Montpellier", "416 Rue du Mas de Verchant, 34000 Montpellier", "https://ecole-ecs.com""\n")
    creer_label_ecole(content_frame, "EICAR Paris (École Internationale de Création Audiovisuelle et de Réalisation)", "16 Rue de l'École de Médecine, 75006 Paris", "https://www.eicar.fr/""\n")
    creer_label_ecole(content_frame, "ISTDS (Institut Supérieur des Techniques du Son)", "51 Rue de Paris, 94220 Charenton-le-Pont", "https://esra.edu/""\n")

    labelDom13 = Label(content_frame, text="\n\n Informatique \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom13.pack()
    creer_label_ecole(content_frame, "École Polytechnique - Département d'Informatique", "Route de Saclay, 91128 Palaiseau Cedex, France.", "http://www.enseignement.polytechnique.fr/""\n")
    creer_label_ecole(content_frame, "ENSEIRB-MATMECA - Électronique, Informatique, Télécommunications", "1 Avenue du Dr Albert Schweitzer, 33402 Talence Cedex, France.", "http://www.enseirb-matmeca.fr""\n")
    creer_label_ecole(content_frame, "EPITA - École pour l'Informatique et les Techniques Avancées", "14-16 Rue Voltaire, 94276 Le Kremlin-Bicêtre Cedex, France.", "https://www.epita.fr""\n")
    creer_label_ecole(content_frame, "INSA Lyon - Département Informatique", "20 Avenue Albert Einstein, 69621 Villeurbanne Cedex, France.", "https://if.insa-lyon.fr/""\n")
    creer_label_ecole(content_frame, "Télécom Paris - Département Informatique", "19 Place Marguerite Perey, 91120 Palaiseau, France.", "https://www.telecom-paris.fr""\n")
    creer_label_ecole(content_frame, "ESIEE Paris - École d'Ingénieurs en Informatique, Électronique et Électrotechnique", "2 Boulevard Blaise Pascal, 93160 Noisy-le-Grand, France.", "https://www.esiee.fr""\n")
    creer_label_ecole(content_frame, "EPITECH - École pour l'Informatique et les Nouvelles Technologies", "24 Rue Pasteur, 94270 Le Kremlin-Bicêtre, France.", "https://www.epitech.eu""\n")
    creer_label_ecole(content_frame, "42 Paris - École d'Informatique", "96 Boulevard Bessières, 75017 Paris, France.", "https://www.42.fr""\n")
    creer_label_ecole(content_frame, "ENSEA - École Nationale Supérieure de l'Électronique et de ses Applications", "6 Avenue du Ponceau, 95014 Cergy-Pontoise Cedex, France.", "https://www.ensea.fr""\n")
    creer_label_ecole(content_frame, "Supinfo - École d'Informatique", "90 Rue Adolphe Coll, 31300 Toulouse, France.", "https://www.supinfo.com/""\n")

    labelDom14 = Label(content_frame, text="\n\n Lettres \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom14.pack()
    creer_label_ecole(content_frame, "Université Paris-Sorbonne - UFR de Littérature française et comparée", "1 Rue Victor Cousin, 75005 Paris", "https://lettres.sorbonne-universite.fr/faculte-des-lettres/ufr/ufr-de-litterature-francaise-et-comparee""\n")
    creer_label_ecole(content_frame, "Université Paris 3 Sorbonne Nouvelle - UFR de Littérature comparée et de Linguistique", "13 Rue de Santeuil, 75005 Paris", "http://www.univ-paris3.fr""\n")
    creer_label_ecole(content_frame, "Université Paris 7 Diderot - UFR de Littérature française et comparée", "5 Rue Thomas Mann, 75013 Paris", "http://www.univ-paris-diderot.fr""\n")
    creer_label_ecole(content_frame, "Université Lyon 2 Lumière - Département de Lettres modernes", "18 Quai Claude Bernard, 69007 Lyon", "https://www.univ-lyon2.fr""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - Faculté des Lettres", "9 Place de l'Université, 67000 Strasbourg", "https://www.unistra.fr""\n")
    creer_label_ecole(content_frame, "Université Aix-Marseille - Faculté des Arts, Lettres, Langues et Sciences Humaines", "29 Avenue Robert Schuman, 13621 Aix-en-Provence", "https://www.univ-amu.fr""\n")
    creer_label_ecole(content_frame, "Université Toulouse - Jean Jaurès - Département Lettres et Langues", "5 Allées Antonio Machado, 31058 Toulouse", "https://www.univ-tlse2.fr""\n")
    creer_label_ecole(content_frame, "Université de Nantes - UFR Lettres et Langages", "Chemin de la Censive du Tertre, 44000 Nantes", "https://www.univ-nantes.fr""\n")
    creer_label_ecole(content_frame, "Université de Lorraine - Faculté des Lettres", "23 Boulevard Albert 1er, 54000 Nancy", "https://www.univ-lorraine.fr""\n")
    creer_label_ecole(content_frame, "Université de Bordeaux - UFR Lettres et Sciences humaines", "3 Ter Place de la Victoire, 33076 Bordeaux", "https://www.u-bordeaux.fr""\n")

    labelDom15 = Label(content_frame, text="\n\n Transportrs \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom15.pack()
    creer_label_ecole(content_frame, "IUT de Sceaux - Département Logistique et Transport", "8 Avenue de la Division Leclerc, 92330 Sceaux, France", "https://www.iut-sceaux.universite-paris-saclay.fr/""\n")
    creer_label_ecole(content_frame, "ESLI - École Supérieure de Logistique Industrielle", "33 Avenue René Cassin, 92380 Garches, France", "https://www.faq-logistique.com/Esli.htm""\n")
    creer_label_ecole(content_frame, "EMLV - Option Transport et Logistique", "12 Avenue Léonard de Vinci, 92400 Courbevoie, France", "https://www.emlv.fr/""\n")
    creer_label_ecole(content_frame, "IUT de Saint-Dié-des-Vosges - Département Gestion Logistique et Transport", "10 Quai Sadi Carnot, 88100 Saint-Dié-des-Vosges, France", "https://iutsd.univ-lorraine.fr/""\n")
    creer_label_ecole(content_frame, "ENSM - Option Logistique et Transport", "2 Rue Duguay-Trouin, 56100 Lorient, France", "https://www.supmaritime.fr""\n")
    creer_label_ecole(content_frame, "SUPDELOG - Institut Supérieur de Logistique Industrielle", "1 Rue du Maréchal Lyautey, 54500 Vandœuvre-lès-Nancy, France", "https://www.studyrama.com/""\n")
    creer_label_ecole(content_frame, "ESTACA -  Option Logistique et Transport", "12 Rue de la Fuye, 93160 Noisy-le-Grand, France", "https://www.estaca.fr""\n")
    creer_label_ecole(content_frame, "ISTELI - Institut Supérieur du Transport et de la Logistique Internationale", "2 Rue de la Petite Montagne, 45100 Orléans, France", "https://www.isteli.fr""\n")
    creer_label_ecole(content_frame, "IUT de Nîmes - Département Logistique", "Rue du Dr Georges Salan, 30000 Nîmes, France", "https://iut-nimes.edu.umontpellier.fr/""\n")
    creer_label_ecole(content_frame, "IUT de Roanne - Département Gestion Logistique et Transport", "56 Cours de la République, 42300 Roanne, France", "https://iut-roanne.univ-st-etienne.fr/fr/index.html""\n")

    labelDom16 = Label(content_frame, text="\n\n Industrie \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom16.pack()
    creer_label_ecole(content_frame, "MINES ParisTech", "60 Boulevard Saint-Michel, 75006 Paris", "http://www.mines-paristech.fr""\n")
    creer_label_ecole(content_frame, "École des Mines d'Alès", "6 Avenue de Clavières, 30319 Alès", "http://www.mines-ales.fr""\n")
    creer_label_ecole(content_frame, "École Centrale Paris", "Grande Voie des Vignes, 92290 Châtenay-Malabry", "http://www.centralesupelec.fr""\n")
    creer_label_ecole(content_frame, "Arts et Métiers ParisTech", "151 Boulevard de l'Hôpital, 75013 Paris", "https://artsetmetiers.fr""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure de Chimie de Montpellier (ENSCM)", "8 Rue de l'École Normale, 34296 Montpellier Cedex 5", "http://www.enscm.fr""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure de Chimie de Rennes (ENSCR)", "11 Allée de Beaulieu, CS 50837, 35708 Rennes", "http://www.ensc-rennes.fr""\n")
    creer_label_ecole(content_frame, "École Polytechnique", "Route de Saclay, 91128 Palaiseau", "https://www.polytechnique.edu""\n")
    creer_label_ecole(content_frame, "IMT Atlantique - Institut Mines-Télécom", "4 Rue Alfred Kastler, 44300 Nantes", "http://www.imt-atlantique.fr""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure d'Arts et Métiers (ENSAM) - Campus de Cluny", "6 Cours de la République, 71250 Cluny", "http://www.ensam.eu""\n")
    creer_label_ecole(content_frame, "École Supérieure de Physique et de Chimie Industrielles de la Ville de Paris (ESPCI Paris)", "10 Rue Vauquelin, 75005 Paris", "http://www.espci.fr""\n")


    labelDom17 = Label(content_frame, text="\n\n Mécanique \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom17.pack()
    creer_label_ecole(content_frame, "Arts et Métiers ParisTech", "151 Boulevard de l'Hôpital, 75013 Paris, France", "https://artsetmetiers.fr""\n")
    creer_label_ecole(content_frame, "INSA Lyon - Département de Génie Mécanique", "20 Avenue Albert Einstein, 69621 Villeurbanne Cedex, France", "https://www.insa-lyon.fr""\n")
    creer_label_ecole(content_frame, "ENSTA ParisTech - Département de Mécanique des Structures et Matériaux", "828 Boulevard des Maréchaux, 91762 Palaiseau Cedex, France", "http://www.ensta-paristech.fr""\n")
    creer_label_ecole(content_frame, "ISAE-SUPAERO - Institut Supérieur de l'Aéronautique et de l'Espace", "10 Avenue Edouard Belin, 31055 Toulouse Cedex 4, France", "http://www.isae-supaero.fr""\n")
    creer_label_ecole(content_frame, "ENSEIRB-MATMECA - École d'Ingénieurs en Matériaux, Génie Électrique, Automatique", "1 Avenue du Dr Albert Schweitzer, 33402 Talence Cedex, France", "http://www.enseirb-matmeca.fr""\n")
    creer_label_ecole(content_frame, "CentraleSupélec - Génie Mécanique", "3 Rue Joliot-Curie, 91192 Gif-sur-Yvette Cedex, France", "http://www.centralesupelec.fr""\n")
    creer_label_ecole(content_frame, "ESTACA - École Supérieure des Techniques Aéronautiques et de Construction Automobile - Option Mécanique", "12 Rue de la Fuye, 93160 Noisy-le-Grand, France", "https://www.estaca.fr""\n")
    creer_label_ecole(content_frame, "ENSEA - École Nationale Supérieure de l'Électronique et de ses Applications - Option Systèmes Mécaniques", "6 Avenue du Ponceau, 95014 Cergy-Pontoise Cedex, France", "https://www.ensea.fr""\n")
    creer_label_ecole(content_frame, "EPF - École d'Ingénieurs - Option Génie Mécanique et Matériaux", "3 bis Rue Léon Jost, 75017 Paris, France", "https://www.epf.fr""\n")
    creer_label_ecole(content_frame, "ESILV - École Supérieure d'Ingénieurs Léonard de Vinci - Département Mécanique Numérique", "12 Avenue Léonard de Vinci, 92916 Paris La Défense, France", "https://www.esilv.fr""\n")


    labelDom18 = Label(content_frame, text="\n\n Sports et SAnté \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom18.pack()
    creer_label_ecole(content_frame, "Université Paris-Sud - UFR STAPS", "62 Avenue de la Division Leclerc, 92400 Ivry-sur-Seine", "https://www.universite-paris-saclay.fr""\n")
    creer_label_ecole(content_frame, "INSEP (Institut National du Sport, de l'Expertise et de la Performance)", "11 Avenue du Tremblay, 75012 Paris", "https://www.insep.fr""\n")
    creer_label_ecole(content_frame, "Université Lyon 1 - UFR STAPS", "27-29 Boulevard du 11 Novembre 1918, 69622 Villeurbanne", "https://ufr-staps.univ-lyon1.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - UFR STAPS", "14 Rue René Descartes, 67000 Strasbourg", "https://www.unistra.fr""\n")
    creer_label_ecole(content_frame, "Université de Nantes - UFR STAPS", "25 Bis Rue Michel Ange, 44200 Nantes", "https://www.univ-nantes.fr""\n")
    creer_label_ecole(content_frame, "Université Aix-Marseille - UFR STAPS", "163 Avenue de Luminy, 13009 Marseille", "https://fss.univ-amu.fr/fr""\n")
    creer_label_ecole(content_frame, "Université de Montpellier - UFR STAPS", "700 Avenue du Pic Saint-Loup, 34090 Montpellier", "https://staps.edu.umontpellier.fr/""\n")
    creer_label_ecole(content_frame, "Université de Lille - UFR STAPS", "9 Rue de l'Université, 59790 Ronchin", "https://staps.univ-lille.fr""\n")
    creer_label_ecole(content_frame, "Université de Bordeaux - UFR STAPS", "146 Rue Léo Saignat, 33076 Bordeaux", "https://www.u-bordeaux.fr""\n")
    creer_label_ecole(content_frame, "Université Toulouse III - Paul Sabatier - UFR STAPS", "118 Route de Narbonne, 31062 Toulouse", "https://f2smh.univ-tlse3.fr/scolarite""\n")
    creer_label_ecole(content_frame, "Université Pierre et Marie Curie (UPMC) - UFR de Biologie", "4 Place Jussieu, 75005 Paris, France.", "https://www.sorbonne-universite.fr""\n")

    labelDom19 = Label(content_frame, text="\n\n Biologie \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom19.pack()
    creer_label_ecole(content_frame, "Aix-Marseille Université - Faculté des Sciences de Luminy - Département de Biologie", "163 Avenue de Luminy, 13288 Marseille Cedex 09, France.", "https://sciences.univ-amu.fr/fr/departements/biologie""\n")
    creer_label_ecole(content_frame, "Université Claude Bernard Lyon 1 - UFR de Biologie", "43 Boulevard du 11 Novembre 1918, 69622 Villeurbanne Cedex, France.", "https://www.univ-lyon1.fr""\n")
    creer_label_ecole(content_frame, "Université Paris-Sud - UFR Sciences - Département de Biologie", "Bâtiment 360, 91405 Orsay Cedex, France.", "https://www.universite-paris-saclay.fr""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - UFR des Sciences de la Vie", "4 Rue Blaise Pascal, 67081 Strasbourg Cedex, France.", "https://www.unistra.fr""\n")
    creer_label_ecole(content_frame, "Université de Bordeaux - UFR Sciences de la Vie et de la Terre", "351 Cours de la Libération, 33405 Talence Cedex, France.", "https://www.u-bordeaux.fr""\n")
    creer_label_ecole(content_frame, "Université de Lille - UFR Biologie", "1 Place Déliot, 59000 Lille, France.", "https://sciences-technologies.univ-lille.fr/biologie""\n")
    creer_label_ecole(content_frame, "Université de Nantes - UFR des Sciences et des Techniques - Département de Biologie", "2 Rue de la Houssinière, 44322 Nantes Cedex 3, France.", "https://www.univ-nantes.fr""\n")
    creer_label_ecole(content_frame, "Université de Montpellier - UFR des Sciences", "Place Eugène Bataillon, 34095 Montpellier Cedex 5, France.", "https://www.umontpellier.fr""\n")
    creer_label_ecole(content_frame, "MINES ParisTech", "60 Boulevard Saint-Michel, 75006 Paris", "https://www.mines-paristech.fr""\n")
    creer_label_ecole(content_frame, "École Centrale Paris", "Grande Voie des Vignes, 92290 Châtenay-Malabry", "https://www.centralesupelec.fr""\n")
    creer_label_ecole(content_frame, "ENSE3 (École Nationale Supérieure de l'Énergie, l'Eau et l'Environnement)", "21 Avenue des Martyrs, 38000 Grenoble", "https://ense3.grenoble-inp.fr""\n")

    labelDom20 = Label(content_frame, text="\n\n Énergie \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom20.pack()
    creer_label_ecole(content_frame, "ICAM (Institut Catholique d'Arts et Métiers) - Campus de Lille", "6 Rue Auber, 59000 Lille", "https://www.icam.fr/lille""\n")
    creer_label_ecole(content_frame, "INP-ENSEEIHT ", "2 Rue Charles Camichel, 31071 Toulouse", "https://www.enseeiht.fr""\n")
    creer_label_ecole(content_frame, "ENSTA Paris", "32 Boulevard Victor, 75739 Paris Cedex 15", "https://www.ensta-paris.fr""\n")
    creer_label_ecole(content_frame, "ENSE3 - Ecole Nationale Supérieure de l'Energie, l'Eau et l'Environnement (Grenoble INP)", "21 Avenue des Martyrs, 38000 Grenoble", "https://ense3.grenoble-inp.fr""\n")
    creer_label_ecole(content_frame, "ESIGELEC (École Supérieure d'Ingénieurs en Génie Électrique)", "Avenue Galilée, 76800 Saint-Étienne-du-Rouvray", "https://www.esigelec.fr""\n")
    creer_label_ecole(content_frame, "IFP School", "232 Avenue Napoléon Bonaparte, 92852 Rueil-Malmaison Cedex", "https://www.ifp-school.com""\n")
    creer_label_ecole(content_frame, "Mines Saint-Étienne - École Nationale Supérieure des Mines de Saint-Étienne", "158 Cours Faur", "https://www.mines-stetienne.fr""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure de Chimie de Montpellier (ENSCM)", "8 Rue de l'École Normale, 34296 Montpellier Cedex 5, France.", "https://www.enscm.fr""\n")
    creer_label_ecole(content_frame, "Chimie ParisTech (École Nationale Supérieure de Chimie de Paris)", "11 Rue Pierre et Marie Curie, 75005 Paris, France.", "https://www.chimieparistech.psl.eu""\n")
    creer_label_ecole(content_frame, "École Nationale Supérieure de Chimie de Rennes (ENSCR)", "11 Allée de Beaulieu, CS 50837, 35708 Rennes Cedex 7, France.", "https://www.ensc-rennes.fr""\n")

    labelDom21 = Label(content_frame, text="\n\n Chimie \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom21.pack()
    creer_label_ecole(content_frame, "Institut de Chimie et des Matériaux Paris-Est (ICMPE)", "2-8 Rue Henri Dunant, 94320 Thiais, France.", "https://www.icmpe.cnrs.fr/""\n")
    creer_label_ecole(content_frame, "ENSCL - École Nationale Supérieure de Chimie de Lille", "Cité Scientifique - CS 90108, 59652 Villeneuve-d'Ascq Cedex, France.", "https://www.univ-lille.fr/enscl""\n")
    creer_label_ecole(content_frame, "Institut Charles Gerhardt Montpellier - UMR 5253", "Place Eugène Bataillon, CC 1501, 34095 Montpellier Cedex 5, France.", "https://www.icgm.fr""\n")
    creer_label_ecole(content_frame, "Institut Lavoisier de Versailles (ILV)", "45 Avenue des États-Unis, 78035 Versailles Cedex, France.", "https://www.ilv.uvsq.fr/""\n")
    creer_label_ecole(content_frame, "Institut des Sciences Moléculaires d'Orsay (ISMO)", "Université Paris-Sud, Bâtiment 351, 91405 Orsay Cedex, France.", "http://www.ismo.universite-paris-saclay.fr/""\n")
    creer_label_ecole(content_frame, "Institut de Chimie Moléculaire de Reims (ICMR)", "51687 Reims Cedex 2, France.", "https://www.univ-reims.fr/icmr/""\n")
    creer_label_ecole(content_frame, "Institut de Chimie de Nice (ICN)", "Parc Valrose, 06108 Nice Cedex 2, France.", "https://imredd.fr/lab/icn/""\n")

    labelDom22 = Label(content_frame, text="\n\n Mathématiques \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom22.pack()

    creer_label_ecole(content_frame, "ENS (École Normale Supérieure) - Département de Mathématiques et Applications", "45 Rue d'Ulm, 75005 Paris, France.", "https://www.math.ens.fr/""\n")
    creer_label_ecole(content_frame, "Université Pierre et Marie Curie (UPMC) - UFR de Mathématiques", "4 Place Jussieu, 75005 Paris, France.", "https://www.math.upmc.fr/""\n")
    creer_label_ecole(content_frame, "Institut des Hautes Études Scientifiques (IHÉS) - Mathématiques", "Le Bois-Marie, 35 Route de Chartres, 91440 Bures-sur-Yvette, France.", "https://www.ihes.fr/""\n")
    creer_label_ecole(content_frame, "Institut Fourier - Université Grenoble Alpes - Mathématiques et Informatique", "100 Rue des Maths, 38402 Saint-Martin-d'Hères, France.", "https://www-fourier.ujf-grenoble.fr/""\n")
    creer_label_ecole(content_frame, "Institut Henri Poincaré (IHP) - Mathématiques", "11 Rue Pierre et Marie Curie, 75005 Paris, France.", "https://www.ihp.fr/""\n")
    creer_label_ecole(content_frame, "Université de Rennes 1 - UFR de Mathématiques", "263 Avenue du Général Leclerc, 35042 Rennes Cedex, France.", "https://math.univ-rennes.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - UFR de Mathématiques", "7 Rue René Descartes, 67084 Strasbourg Cedex, France.", "https://www.math.unistra.fr/""\n")
    creer_label_ecole(content_frame, "École Polytechnique - Département de Mathématiques", "Route de Saclay, 91128 Palaiseau Cedex, France.", "https://www.math.polytechnique.fr/""\n")
    creer_label_ecole(content_frame, "Université de Nantes - UFR de Mathématiques", "2 Rue de la Houssinière, 44322 Nantes Cedex 3, France.", "https://www.math.sciences.univ-nantes.fr/""\n")
    creer_label_ecole(content_frame, "Institut de Mathématiques de Jussieu - Paris Rive Gauche (IMJ-PRG)", "4 Place Jussieu, 75005 Paris, France.", "https://www.imj-prg.fr/""\n")


    labelDom23 = Label(content_frame, text="\n\n Physique \n\n", font= ("arial",25), fg ="#2F699C", bg="#9c742f")
    labelDom23.pack()

    creer_label_ecole(content_frame, "ENS (École Normale Supérieure) - Département de Physique", "24 Rue Lhomond, 75005 Paris, France.", "https://www.phys.ens.fr/""\n")
    creer_label_ecole(content_frame, "Université Pierre et Marie Curie (UPMC) - UFR de Physique", "4 Place Jussieu, 75005 Paris, France.", "https://sciences.sorbonne-universite.fr/faculte/ufr-instituts-observatoires-ecoles/ufr-de-physique""\n")
    creer_label_ecole(content_frame, "École Polytechnique - Département de Physique", "Route de Saclay, 91128 Palaiseau Cedex, France.", "https://portail.polytechnique.edu/physique/fr/accueil""\n")
    creer_label_ecole(content_frame, "Institut d'Optique Graduate School - Laboratoire Charles Fabry", "Campus Polytechnique, 2 Avenue Augustin Fresnel, 91127 Palaiseau Cedex, France.", "https://www.institutoptique.fr/""\n")
    creer_label_ecole(content_frame, "Université de Strasbourg - UFR de Physique et Ingénierie", "3 Rue de l'Université, 67000 Strasbourg, France.", "https://physique-ingenierie.unistra.fr/""\n")
    creer_label_ecole(content_frame, "Université Paris-Sud - UFR Sciences - Département de Physique", "Bâtiment 430, 91405 Orsay Cedex, France.", "https://www.phys.universite-paris-saclay.fr/""\n")
    creer_label_ecole(content_frame, "ENS Lyon (École Normale Supérieure de Lyon) - Département de Physique", "46 Allée d'Italie, 69364 Lyon Cedex 07, France.", "https://www.ens-lyon.fr/PHYSIQUE""\n")
    creer_label_ecole(content_frame, "Université de Bordeaux - UFR Sciences et Technologies - Département de Physique", "351 Cours de la Libération, 33405 Talence Cedex, France.", "https://www.u-bordeaux.fr/""\n")
    creer_label_ecole(content_frame, "Université de Lille - UFR de Physique", "1 Place Déliot, 59000 Lille, France.", "https://sciences-technologies.univ-lille.fr/""\n")
    creer_label_ecole(content_frame, "Université Paris Diderot - UFR de Physique", "10 Rue Alice Domon et Léonie Duquet, 75013 Paris, France.", "https://physique.univ-paris-diderot.fr/""\n")


    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    #centrer_fenetre(fenetre, 900, 670)

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))



    fenetre.mainloop()


def boutonFourreTout():

    fenetre.destroy()

    return(0)

def favorits():    
    fin = Tk()
    connexion = sqlite3.connect('pole_ecole.db')
    c = connexion.cursor()
    
	###Le fonction qui permet de supprimer une ligne
    def cancella():
            selezione = tv.selection()[0]
            mb_canc = messagebox.askokcancel(
                title="Confirmer la suppression",
                message="Voulez-vous confirmer l'élimination?")
            if mb_canc == True:
                tv.delete(selezione)
                for st in selezione:
                    k = int(selezione[-1]) - 1
                c.execute("SELECT nom_ecole,lien,adresse FROM sauvegarde")
                v = c.fetchall()
                ecole = v[k][2]
                c.execute("SELECT nom_ecole,lien,adresse FROM sauvegarde WHERE nom_ecole = '"+ecole+"'")


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
    c.execute("SELECT nom_ecole,lien,adresse FROM sauvegarde")
    favoris = c.fetchall()
    for i in favoris:
        eco = i[0]
        url = i[1]
        adr = i[2]
        print(eco,url,adr)
        tv.insert("", 0, values=(adr, eco, url))

        #Met le bouton qui supprime renvoie a la fonction cancella
    puls_canc = ttk.Button(fin, text="Supprimer", command=cancella)
    puls_canc.pack()


# CORPS PRINCIPAL DU PROGRAMME

fenetre = Tk()
fenetre.title("Pôle école")
fenetre.geometry("600x400")
fenetre.configure(bg='#9c742f')

# - - - - - C'est sur cette zone qu'on définit une Frame - - - -


zone1 = Frame(fenetre)
zone2 = Frame(fenetre, bg='#573f17')

label = Label(zone1, text="À la recherche de ton Future?",font=("arial", 30),fg="white")
label.config(bg="#9c742f")
label.pack()

bouBleua = Button(zone2, text="Les métiers", fg="white", bg="#BBBB55", command = metiers)

bouBleub = Button(zone2, text="Les formations", fg="white", bg='#BBBB55', command = ecoles)

bouBleuc = Button(zone2, text="Vos favoris", fg="white", bg='#BBBB55', command = favorits)


zone1.pack(fill=Y, padx=30,pady=60)
zone2.pack(fill=Y, padx=10,pady=10)

bouBleua.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)
bouBleub.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)
bouBleuc.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)



fenetre.mainloop()
