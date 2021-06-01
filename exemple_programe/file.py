# DOCUMENT STATISTIQUES


# Création d'un fichier txt
#f = open("fichier_statistiques.txt","x")


#f = open("fichier_statistiques.txt", "a") # Ouverture du fichier
#f.write("Bonjour") # Ecriture dans le fichier
#f.close() # Fermeture du fichier

x = 10 # Nombre de personnes

f = open("fichier_statistiques.txt", "w") # Ouverture du fichier
f.write("DOCUMENT STATISTIQUES \n\n ") # suppression et reecriture dans le fichier
f.write("Nombre de personnes : ")
f.write(str(x)) # Conversion du nombre en string
f.close() # Fermeture du fichier

# Ouverture et lecture du fichier après ajout de texte
f = open("fichier_statistiques.txt", "r")
print(f.read())



