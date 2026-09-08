import kagglehub
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
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
#print(data.describe())


data = data.loc[(data['Year'] != 2019)  & (data['Year'] != 2020)] #filtro retirando dados de 2019 e 2020, pois estavam com dados vazios


#tamanho da img
plt.figure(figsize=(13,5))
#titulo da img
plt.title ('Quantidade de vendas globais por ano (mi)', loc = 'left', fontsize = 14 )
#Gráfico
sns.barplot(data= data, x = 'Year', y = 'Global', errorbar= None, estimator=sum) #errorbar = None tira a barra vertical de desv, estimator = sum faz a soma de cada ano
#legenda
plt.xlabel ('Quantidades de vendas (mi)')
#plt
#plt.show()

print(data.columns)

plt.figure(figsize=(13,5))
plt.style.use('ggplot')

plt.title('Distribuiçao das vendas globais', loc='left', fontsize = 14)
sns.kdeplot(data['Global'], fill = True, bw_method = 1, linewidth = 2.5) #fill = adiciona sombra abaixo da linha

#plt.show()
Analise = data.groupby(by =['Year']).sum()
#print (Analise)

plt.figure(figsize= (13,5))
plt.title('Análise da distribuição global (mi)', loc= 'left', fontsize = 14)
sns.boxplot(data= data, x ='Year', y='Global')

#print (data.loc[ data['Global'] >= 10])

#Gráfico mostrnado % de vendas por pais comparado ao total, barras empilhadas

America = [ America / Total * 100 for America, Total in zip(Analise['North America']  , Analise ['Global'] )]
Europa = [ Europa / Total * 100 for Europa, Total in zip(Analise['Europe']  , Analise ['Global'] )]
Japao = [ Japao / Total * 100 for Japao, Total in zip(Analise['Japan']  , Analise ['Global'] )]
Mundo = [ Mundo / Total * 100 for Mundo, Total in zip(Analise['Rest of World']  , Analise ['Global'] )]

#print (America, Europa, Japao, Mundo)

plt.figure(figsize= (13,5))

largura = 0.8
rotulos = [Analise.index] 
grupos = [0, 1, 2, 3, 4, 5 ]
plt.title('Analise distribuiçao por continente', loc='left', fontsize = 14 )
#Plot America
plt.bar(grupos, America, width= largura, color = '#b5ffb9', edgecolor = 'white')
#Plot Europa
plt.bar(grupos, Europa,bottom= America, width= largura, color = '#f9bc86', edgecolor = 'white')
#Plot Japão
plt.bar(grupos, Japao,bottom= [A + B for A, B in zip(America, Europa)], width= largura, color = '#a3acff', edgecolor = 'white')
#Plot Mundo
plt.bar(grupos, Mundo,bottom= [A + B + C for A, B, C in zip(America, Europa, Japao)], width= largura, color = '#d3acfe', edgecolor = 'white')

plt.xticks (grupos, Analise.index)
plt.xlabel ('Grupo')
plt.ylabel ('Distribuição %')
plt.legend (['América do Norte', 'Europa', 'Japão', 'Mundo'], bbox_to_anchor = (0.7, -0.1), ncol = 4)


label = LabelEncoder() #LabelEncoder serve para transformar cada valor escrito em um valor numérico, adicionando identificadores numericos unicos

data['Produtora'] = label.fit_transform(data['Publisher'])
data['Genero'] = label.fit_transform(data['Genre'])
data['Jogo'] = label.fit_transform(data['Game'])

print(data.head())

cores = sns.color_palette('husl', 8)
print (cores)


#plt.show()
