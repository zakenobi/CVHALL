import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show, figure

path = ("exemple_programe\stat_CS\donnee.csv")
df = pd.read_csv(path,sep=';',index_col=1)
dp = df[['Somme_avec_masques','Somme_non_masques']].iloc[[0]]

fig = plt.figure(figsize=(8, 6), dpi=80)

# Pie

labels = [dp.iloc[0][0],dp.iloc[0][1]]
sum1 = dp.iloc[0][0].sum()
sum2= dp.iloc[0][1].sum()

sum_masque = df['Somme_avec_masques'] = df['nb_masques_bien_portes'].sum()
sum_Nmasque = df['Somme_sans_masques'] = df['nb_masques_non_portes'].sum()

labels = [sum_masque,sum_Nmasque]

slices = [sum_masque,sum_Nmasque]

plt.pie(slices, labels = labels)
plt.title('Proportion de sujets portant leur masque ou non')
plt.legend(['Masque porté','Masque non porté'],loc = "lower left", facecolor = "lightgray")
plt.savefig("app/resources/Pie")

# Histogramme 

hours = df.groupby('Heures').agg('sum')
hours = hours[['nb_masques_bien_portes','nb_masques_non_portes']]
hours.plot.bar()
plt.title("Nombre de détections en fonction de l'heure")
plt.savefig("app/resources/Histogram")
plt.legend(["Masques bien portés","Masques mal portés"],loc = "upper right", facecolor = "lightgray")
plt.show()


   