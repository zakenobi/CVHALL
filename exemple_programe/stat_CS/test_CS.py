
import pandas as pd
from matplotlib.pyplot import pie, axis, show 
import matplotlib.pyplot as plt 




#df = pd.read_csv ('chart_work.csv')

#sums = df.groupby(df["Product Name;"])["Number Of Bugs"].sum()
#axis('equal');
#pie(sums, labels=sums.index);
#show()

#ouverture et lecture du fichier type

file = '/Users/mathieu/ProjetChallenge/CVHALL/exemple_programe/stat_CS/donnee.csv'
df = pd.read_csv(file,sep=';',index_col=0)
print(df.head(2))
print(df[["nb_personnes"]])

#Création du pie.plot
my_labels=['Avec masque','Sans masque']
sums = df.groupby(df["nb_masques_bien_portes"])["nb_masques_non_portes"].sum()
#axis('equal')
#axis('nombre de personnes avec masque')
pie(sums,labels=my_labels)
#df.pie(subplots = False, title="Repartition de personnes avec et sans masques",y='nb_masques_non_portes', labels = my_labels).legend(bbox_to_anchor=(0.90, 0.8))

#Second plot 

#df.plot.pie(title="Repartition de personnes avec et sans masques",y='nb_masques_non_portes', labels = my_labels).legend(bbox_to_anchor=(0.90, 0.8))

#ax1 = plt.axes()
#ax1.xaxis.label.set_visible(False)
#df.plot.axis("Tk le plus beau")
#plt.pie(df["nb_masques_bien_portes"]["nb_masques_non_portes"])

plt.show()


