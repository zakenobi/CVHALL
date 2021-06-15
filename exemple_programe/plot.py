import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show 
import pandas as pd

path = ("/Users/mathieu/ProjetChallenge/CVHALL/exemple_programe/stat_CS/donnee.csv")
df = pd.read_csv(path,sep=';',index_col=1)
#print(df.head())
dp = df[['Somme_avec_masques','Somme_non_masques']].iloc[[0]]
#print(dp)
labels = ['Somme_avec_masques','Somme_non_masques']
fig = plt.figure()


labels = [dp.iloc[0][0],dp.iloc[0][1]]
sum1 = dp.iloc[0][0].sum()
sum2= dp.iloc[0][1].sum()
slices = [sum1,sum2]
#plt.pie(slices, labels = labels)
#plt.title('Proportion de sujets portant leur masque ou non')
#plt.legend(['Masque porté','Masque non porté'],loc = "lower left", facecolor = "lightgray")
#plt.savefig("app/resources/Figure")

#Histogramme 

hours = df.groupby('Heures').agg('sum')
hours = hours[['nb_masques_bien_portes','nb_masques_non_portes']]
print(hours)
#plt.hist(x=hours.index.values)
plt.hist(hours)
hours.plot.bar()
print(df.index.values)
plt.show()