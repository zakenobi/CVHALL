
import pandas as pd

file = '/Users/mathieu/ProjetChallenge/CVHALL/exemple_programe/stat_CS/donnee.csv'
df = pd.read_csv(file,sep=';',index_col=0)
df.head(5)
