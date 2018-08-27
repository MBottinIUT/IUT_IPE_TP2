#!usr/bin/python3
# -*- coding : utf-8 -*-
from De import De_a_jouer
import time

"""
Module IPE - TPs Raspberry
auteurs : Noms des etudiants
Etablissement : IUT de Rennes - Dpt GEII

Commentaires : 
"""

def Lancer() :
	# Determination des deux lancers
	valeur_de1_joueur=de1_joueur.lancer_de()
	valeur_de2_joueur=de2_joueur.lancer_de()
	fichier_de1_joueur = "die_face_"+str(valeur_de1_joueur)+"_T.png"
	fichier_de2_joueur = "die_face_"+str(valeur_de2_joueur)+"_T.png"
	image_de1_joueur.image = fichier_de1_joueur
	image_de2_joueur.image = fichier_de2_joueur
	time.sleep(1)
	valeur_de1_raspberry=de1_raspberry.lancer_de()
	valeur_de2_raspberry=de2_raspberry.lancer_de()
	fichier_de1_raspberry = "die_face_"+str(valeur_de1_raspberry)+"_T.png"
	fichier_de2_raspberry = "die_face_"+str(valeur_de2_raspberry)+"_T.png"
	image_de1_raspberry.image = fichier_de1_raspberry
	image_de2_raspberry.image = fichier_de2_raspberry
	# Determination du gagnant
	if (de1_joueur.valeur + de2_joueur.valeur) > (de1_raspberry.valeur + de2_raspberry.valeur) :
		image_joueur.image = "win.png"
		image_raspberry.image = "lose.png"
	elif (de1_joueur.valeur + de2_joueur.valeur) < (de1_raspberry.valeur + de2_raspberry.valeur) :
		image_joueur.image = "lose.png"
		image_raspberry.image = "win.png"
	else :
		image_joueur.image = "question-mark.png"
		image_raspberry.image = "question-mark.png"
	fenetre.display()


de1_joueur = De_a_jouer()
de2_joueur = De_a_jouer()
de1_raspberry = De_a_jouer()
de2_raspberry = De_a_jouer()

# On importe guizero (wrapper de Tkinter)
import guizero

# On cree une fenetre, racine de notre interface
fenetre = guizero.App(title = "Exercice 08", height=480, width=600, layout="grid")

# Mise en place du layout
titre = guizero.Text(fenetre, text= "Bienvenue dans ce jeu de des !!", grid=[1,0], align="top")
image_titre = guizero.Picture(fenetre, image="Anime_rolling_dice_2.gif", grid=[1,1])
titre_joueur = guizero.Text(fenetre, text= "Vous :", grid=[0,2], align="left")
bouton_joueur = guizero.PushButton(fenetre, text= "Lancer", grid=[1,2], command = Lancer)
image_de1_joueur = guizero.Picture(fenetre, image="die_face_1_T.png", grid=[0,3])
image_de2_joueur = guizero.Picture(fenetre, image="die_face_1_T.png", grid=[1,3])
image_joueur = guizero.Picture(fenetre, image="question-mark.png", grid=[2,3])
titre_raspberry = guizero.Text(fenetre, text= "Raspberry :", grid=[0,4], align="left")
image_de1_raspberry = guizero.Picture(fenetre, image="die_face_1_T.png", grid=[0,5])
image_de2_raspberry = guizero.Picture(fenetre, image="die_face_1_T.png", grid=[1,5])
image_raspberry = guizero.Picture(fenetre, image="question-mark.png", grid=[2,5])


# programme principal
fenetre.display()
 
# (dans geany, choisir python3 pour exécuter les programmes)

