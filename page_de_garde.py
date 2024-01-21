from tkinter import *

# DEFINITIONS DES FONCTIONS

def boutonFourreTout():

    fenetre.destroy()

    return(0)

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

bouBleua = Button(zone2, text="Les métiers", fg="white", bg="#BBBB55", command = boutonFourreTout)

bouBleub = Button(zone2, text="Les formations", fg="white", bg='#BBBB55', command = boutonFourreTout)

bouBleuc = Button(zone2, text="Vos favoris", fg="white", bg='#BBBB55', command = boutonFourreTout)


zone1.pack(fill=Y, padx=30,pady=60)
zone2.pack(fill=Y, padx=10,pady=10)

bouBleua.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)
bouBleub.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)
bouBleuc.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)



fenetre.mainloop()