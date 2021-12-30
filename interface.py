from tkinter import *

window = Tk()
window.geometry("720x480")
#window.config(background="#41B77F")
window.title("Application")
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=1)

bienvenue=Label(window,text="Bonjour et bienvenue",font=("verdana",20),bg="#41B77F",fg="white")
name=Label(window,text="Mohamed Bourema Traore",font=("verdana",20),bg="#41B77F",fg="white")
bienvenue.pack()

menuBar = Menu(window)
################# MENU FICHIER ##############
menuFichier = Menu(menuBar)
menuFichier.add_command(label="Ouvrir")
menuFichier.add_command(label="Fermer")
menuFichier.add_command(label="Quitter", command=quit)

################# MENU RECONNAISSANCE ##############
menuRec = Menu(menuBar)
menuRec.add_command(label="Par les réseaux de neurones")


################# MENU OUTILS ##############
menuOutils = Menu(menuBar)
menuOutils.add_command(label="Taux d'erreur")
menuOutils.add_command(label="Créer une base d'apprentissage")

################# MENU HELP ##############
menuHelp = Menu(menuBar)
menuHelp.add_command(label="A propos des réseaux de neurones")
menuHelp.add_command(label="A propos de l'interface")

menuBar.add_cascade(label="Fichier",menu=menuFichier)
menuBar.add_cascade(label="Outils",menu=menuOutils)
menuBar.add_cascade(label="Reconnaissance",menu=menuRec)
menuBar.add_cascade(label="Help",menu=menuHelp)


window.config(menu=menuBar,background="#41B77F")
window.mainloop();
