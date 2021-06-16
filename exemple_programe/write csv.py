import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.pyplot import pie, axis, show, figure
from pandas.core.frame import DataFrame

dc = DataFrame(columns=['Date','Heures','nb_masques_bien_portes','nb_masques_non_portes','Somme_avec_masques','Somme_non_masques'])
dc.to_csv(r"exemple_programe\stat_CS\donnee.csv",  index = False,sep=';', encoding='utf-8')