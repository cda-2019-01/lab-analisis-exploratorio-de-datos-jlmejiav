# listprecios = !ls precios/*
import pandas as pd 
import numpy as np 
## definir función para leer
def leer_precios(filename):
    for k in range(10):
        df = pd.read_excel(filename,
                           skiprows = k,
                           usecols = list(range(26)))
        if df.iloc[0,0] == 'Fecha':
            df = pd.read_excel(filename,
                               skiprows = k+1,
                               usecols = list(range(26)))
            break
        
    return(df)
## 
# filenames = !ls precios/
dfs = []
for filename in filenames:
    dfs.append(leer_precios(filename))