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


data = data.loc[(data['Year'] != 2019)  & (data['Year'] != 2020)] #filtro retirando dados de 2019 e 2020, pois estavam com dados vazios


#tamanho da img
plt.figure(figsize=(13,5))
#titulo da img
plt.title ('Quantidade de vendas globais por ano (mi)', loc = 'left', fontsize = 14 )
#Gráfico
sns.barplot(data= data, x = 'Year', y = 'Global', ci = None, estimator=sum) #ci = None tira a barra vertical de desv, estimator = sum faz a soma de cada ano
#legenda
plt.xlabel ('Quantidades de vendas (mi)')
#plt
#plt.show()

#print(data.head())

plt.figure(figsize=(13,5))
plt.style.use('ggplot')

plt.title('Distribuiçao das vendas globais', loc='left', fontsize = 14)
sns.kdeplot(data['Global'], fill = True, bw = 1, linewidth = 2.5) #fill = adiciona sombra abaixo da linha

#plt.show()
print (data.groupby(by =['Year']).sum())

plt.figure(figsize= (13,5))
plt.title('Análise da distribuição global (mi)', loc= 'left', fontsize = 14)
sns.boxplot(data= data, x ='Year', y='Global')

plt.show()

print (data.loc[ data['Global'] >= 10])