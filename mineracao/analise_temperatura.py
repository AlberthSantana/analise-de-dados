import pandas as pd
import numpy as np
import seaborn as sns

#cria um dataframe
df = pd.read_csv('mineracao\Ice Cream Sales - temperatures.csv')

print(df.head())

df_ordenado = df.sort_values(by='Temperature')

print(df_ordenado.head())