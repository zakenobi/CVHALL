from os import truncate
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.pyplot import pie, axis, show, figure
from pandas.core.frame import DataFrame
from matplotlib_venn import venn2

Path(r"exemple_programe/stat_CS/donnee.csv").stat()
file_size =Path(r"exemple_programe/stat_CS/donnee.csv").stat().st_size
print("The file size is:", file_size,"bytes")

path = ("exemple_programe/stat_CS/donnee.csv")
df = pd.read_csv(path,sep=';',index_col=1)
dp = df[['Somme_avec_masques','Somme_non_masques']].iloc[[0]]

# fig = plt.figure(figsize=(8, 6), dpi=80)

    # Pie

labels = [dp.iloc[0][0],dp.iloc[0][1]]
sum1 = dp.iloc[0][0].sum()
sum2= dp.iloc[0][1].sum()

sum_masque = df['Somme_avec_masques'] = df['nb_masques_bien_portes'].sum()
sum_Nmasque = df['Somme_sans_masques'] = df['nb_masques_non_portes'].sum()
print(sum_Nmasque)
denom = sum_masque+sum_Nmasque
sum_masque = 100* (sum_masque/denom)
sum_Nmasque = 100* (sum_Nmasque/denom)
print('===')
sum_masque=float("{0:.2f}".format(sum_masque))
print(sum_masque)

print("Pourcentage de personnes sans masque : %f\nPourcentage de personnes avec masque : %f" %(sum_Nmasque,sum_masque))


labels = [sum_masque,sum_Nmasque]
slices = [sum_masque,sum_Nmasque]
#plt.bar([sum_masque,sum_Nmasque],height=1)
# plt.title('Proportion de sujets portant leur masque ou non')
# plt.legend(['Masque porté','Masque non porté'],loc = "lower left", facecolor = "lightgray")
# plt.savefig("app/resources/Pie")

#Histogramme 
hours = df.groupby('Heures').agg('sum')
hours = hours[['nb_masques_bien_portes','nb_masques_non_portes']]
hours.plot.bar()
plt.title("Nombre de détections en fonction de l'heure")
plt.legend(["Masques bien portés","Masques mal portés"],loc = "upper right", facecolor = "lightgray")
plt.savefig("app/resources/Histogram")
#plt.show()


#On sait que 1 octet = 8 bytes 
if file_size > pow(10,9) : 
    dc = DataFrame(columns=['Date','Heures','nb_masques_bien_portes','nb_masques_non_portes','Somme_avec_masques','Somme_non_masques'])
    dc.to_csv(r"exemple_programe/stat_CS/donnee.csv",  index = False, sep=';', encoding='utf-8')
    print("Fichier CSV écrasé")

else : 
    print("Taille du fichier insuffisant")