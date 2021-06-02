    # DOCUMENT STATISTIQUES


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


    # RECUPERATION DES DONNEES A PARTIR DU FICHIER

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


    # AFFICHAGE DES DONNEES RECUPEREES A PARTIR DU FICHIER

print(ligne4) # Affichage du nombre de personnes
print(ligne6) # Affichage du nombre de personnes avec masque bien porté
print(ligne8) # Affichage du nombre de personnes sans masque
print(ligne10) # Affichage du nombre de personnes avec masque mal porté
print(ligne12) # Affichage du nombre de personnes avec température normale
print(ligne14) # Affichage du nombre de personnes avec température elevée

