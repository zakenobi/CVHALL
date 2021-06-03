    # DOCUMENT STATISTIQUES

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Création d'un fichier txt
#f = open("fichier_statistiques.txt","x")


#f = open("fichier_statistiques.txt", "a") # Ouverture du fichier
#f.write("Bonjour") # Ecriture dans le fichier
#f.close() # Fermeture du fichier


    # INITIALISATION DES VALEURS

nb_personnes = 10 # Nombre de personnes
nb_masques_bien_portes = 7 # Nombre de personnes portant leur masque correctement
nb_masques_non_portes = 1 # Nombre de personnes ne portant pas de masque
nb_masques_mal_portes = 2 # Nombre de personnes portant leur masque incorrectement
nb_temperature_normale = 8 # Nombre de personnes avec une température corporelle normale
nb_temperature_elevee = 2 # Nombre de personnes avec une température corporelle elevee


    # MODIFICATION DU FICHIER

def modification_fichier(): # Création d'une fonction
    f = open("fichier_statistiques.txt", "w") # Ouverture du fichier pour le modifier
    f.write("DOCUMENT STATISTIQUES \n\n") # suppression et reecriture dans le fichier

    f.write("Nombre de personnes : \n")
    f.write(str(nb_personnes)) # Conversion du nombre de personnes en string

    f.write("\nNombre de personnes portant leur masque correctement : \n")
    f.write(str(nb_masques_bien_portes)) # Conversion du nombre en string

    f.write("\nNombre de personnes ne portant pas de masque : \n")
    f.write(str(nb_masques_non_portes)) # Conversion du nombre en string

    f.write("\nNombre de personnes portant leur masque incorrectement : \n")
    f.write(str(nb_masques_mal_portes)) # Conversion du nombre en string

    f.write("\nNombre de personnes avec une température corporelle normale : \n")
    f.write(str(nb_temperature_normale)) # Conversion du nombre en string

    f.write("\nNombre de personnes avec une température corporelle elevée : \n")
    f.write(str(nb_temperature_elevee)) # Conversion du nombre en string

    f.close() # Fermeture du fichier

modification_fichier() # Appel de la fonction


    # RECUPERATION DES DONNEES A PARTIR DU FICHIER

def recuperation_donnees():
    f = open("fichier_statistiques.txt", "r") # Ouverture du fichier pour le lire
    print(f.read()) # Lecture du fichier
    ligne1 = f.readline() # Récupération de la ligne 1 du fichier
    ligne2 = f.readline()
    ligne3 = f.readline()
    ligne4 = f.readline() # Récupération de la ligne 4 du fichier qui correspond au nombre de personnes (nb_personnes)
    ligne5 = f.readline()
    ligne6 = f.readline() # Récupération de la ligne 6 du fichier qui correspond au nombre de masques bien portés (nb_masques_bien_portes)
    ligne7 = f.readline()
    ligne8 = f.readline() # Récupération de la ligne 8 du fichier qui correspond au nombre de personnes sans masque (nb_masques_non_portes)
    ligne9 = f.readline()
    ligne10 = f.readline() # Récupération de la ligne 10 du fichier qui correspond au nombre de masques mal portés (nb_masques_mal_portes)
    ligne11 = f.readline()
    ligne12 = f.readline() # Récupération de la ligne 12 du fichier qui correspond au nombre de personnes avec température normale (nb_temperature_normale)
    ligne13 = f.readline()
    ligne14 = f.readline() # Récupération de la ligne 14 du fichier qui correspond au nombre de personnes avec température elevée (nb_temperature_elevee)
    
recuperation_donnees()



    # GRAPHIQUE STATISTIQUES
from matplotlib import rc
# CAMEMBERT PROPORTION DE MASQUES BIEN/MAL/NON PORTES
y = np.array([nb_masques_bien_portes, nb_masques_mal_portes, nb_masques_non_portes]) # Affectation des valeurs à chaque partie du camembert
mylabels = ["Masques bien portés", "Masques mal portés", "Masques non portés"] # Ajout de nom pour chaque valeur

plt.pie(y, labels = mylabels) # Création du camembert avec les valeurs associées à leur label

font1 = {'family':'serif','color':'darkred','size':12} # Création d'une police d'écriture (taille, couleur...)
font2 = {'family':'serif','color':'k', 'style':'italic','size':10} # Création d'une police d'écriture (taille, couleur...)

plt.legend(title = "Légende :") # Ajout d'une légende avec les labels définis précedemment
plt.title("Porportion de masques bien/mal/non portés", fontdict = font1) # Ajout d'un titre au graph

plt.show() # Affichage du graph


# GRAPHIQUE POURCENTAGE DE MASQUES PORTES CORRECTEMENT AU COURS DE LA JOURNEE
xpoints = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) # Etalage des heures de la journée
ypoints = np.array([15/15*100, 8/10*100, 10/15*100, 10/20*100, 15/20*100, 18/21*100, 15/16*100, 18/20*100, 12/12*100, 16/18*100, 11/12*100, 19/20*100, 10/10*100]) # Pourcentage de masques portés correctement

plt.plot(xpoints, ypoints, marker = 'o') # Création du graph

plt.title("Pourcentage de masques portés correctement au cours de la journée", fontdict = font1) # Ajout d'un titre au graph
plt.xlabel("Heures de la journée", fontdict = font2) # Ajout d'une légende en abscisse
plt.ylabel("Pourcentage de masques portés correctement", fontdict = font2) # Ajout d'une légende en ordonnée

plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5) # Ajout d'un quadrillage

plt.show() # Affichage du graph