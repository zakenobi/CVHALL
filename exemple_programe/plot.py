import pandas as pd
import matplotlib.pyplot as plt


path = ("exemple_programe\stat_CS\donnee.csv")
df = pd.read_csv(path,sep=';',index_col=0)
#print(df.head())
dp = df[['nb_masques_bien_portes','nb_masques_mal_portes']].iloc[[0]]
#print(dp)
labels = ['nb_masques_bien_portes','nb_masques_mal_portes']
fig = plt.figure()

slices = [dp.iloc[0][0],dp.iloc[0][1]]
labels = [dp.iloc[0][0],dp.iloc[0][1]]

plt.pie(slices, labels = labels)
plt.title('Proportion de sujets portant leur masque ou non')
plt.legend(['Masque porté','Masque non porté'],loc = "lower left", facecolor = "lightgray")
plt.savefig("app/resources/Figure")
plt.show()