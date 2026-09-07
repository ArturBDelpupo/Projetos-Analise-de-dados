import kagglehub
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Download latest version
path = kagglehub.dataset_download("sidtwr/videogames-sales-dataset")

file = os.listdir(path)

data = pd.read_csv(os.path.join(path, file[0]), encoding='iso-8859-1')

#print(data.shape)
#print(data.head())
#print (data.isnull().sum())

data = data.dropna()
data = data.drop([])
print(data.describe())

#tamanho da img
plt.figure(figsize=(13,5))

#titulo da img
plt.title ('Quantidade de vendas globais por ano (mi)', loc = 'left', fontsize = 14 )

#Gráfico
sns.barplot(data= data, x = 'Year', y = 'Global', ci = None, estimator=sum) #ci = None tira a barra vertical de desv, estimator = sum faz a soma de cada ano

#legenda
plt.xlabel ('Quantidades de vendas (mi)')

#plt
plt.show()