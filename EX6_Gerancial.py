import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
import os
import numpy
import kagglehub
import seaborn as sns

path = kagglehub.dataset_download("sidtwr/videogames-sales-dataset")
file = os.listdir(path)
data = pd.read_csv(os.path.join(path, file[0]), encoding='latin-1')
data = data.loc[(data['Year'] != 2019)  & (data['Year'] != 2020)] #filtro retirando dados de 2019 e 2020, pois estavam com dados vazios

print(data.head())

label = LabelEncoder() 
data['Produtora'] = label.fit_transform(data['Publisher'])
data['Genero'] = label.fit_transform(data['Genre'])
data['Jogo'] = label.fit_transform(data['Game'])



#Relatório -> Report Gerencial

#Tamanho da imagem
fig = plt.figure(figsize=(15, 8))

#Parametros para o grid
colunas = 2
linhas = 3
#Cor de fundo
#fundo = '#f5f5f5'
#ax.set_facecolor (fundo)
#fig.set_facecolor (fundo)

#Estilo dos graficos
plt.style.use('seaborn-v0_8')
plt.suptitle('Python para análise de dados - Relatório', fontsize = 22, color = '#404040', fontweight= 600) #Titulo relatório
sns.despine(top=True, right=True, left=True, bottom=True)

#Incuindo rodapé do relatório
Rodape = '''
Essse relatório foi elaborado no treinado "Python para Análise de Dados"
Está dispónivel no canal do youtube @Data Viking
by: @Artur Delpupo
github : https://github.com/ArturBDelpupo
'''

fig.text(0.5,-0.02, Rodape, ha='center', va = 'bottom', color = "#393636E7") #Rodapé relatório


#Grafico 1
plt.subplot(linhas, colunas, 1)
#titulo da img
plt.title ('Quantidade de vendas globais por ano (mi)', loc = 'left')
#Gráfico
plt.bar(data= data, x = 'Year', height = 'Global') #errorbar = None tira a barra vertical de desv, estimator = sum faz a soma de cada ano
#legenda
plt.xlabel ('Quantidades de vendas (mi)')

#Grafico 2
plt.subplot(linhas, colunas, 2)
plt.title('Análise da distribuição global (mi)', loc= 'left')
sns.boxplot(data= data, x ='Year', y='Global')

#Grafico 3
Analise = data.groupby(by =['Year']).sum()
plt.subplot(linhas, colunas, 3)
America = [ America / Total * 100 for America, Total in zip(Analise['North America']  , Analise ['Global'] )]
Europa = [ Europa / Total * 100 for Europa, Total in zip(Analise['Europe']  , Analise ['Global'] )]
Japao = [ Japao / Total * 100 for Japao, Total in zip(Analise['Japan']  , Analise ['Global'] )]
Mundo = [ Mundo / Total * 100 for Mundo, Total in zip(Analise['Rest of World']  , Analise ['Global'] )]
#print (America, Europa, Japao, Mundo)
largura = 0.8
rotulos = [Analise.index] 
grupos = [0, 1, 2, 3, 4, 5 ]
plt.title('Analise distribuiçao por continente', loc='left' )
#Plot America
plt.bar(grupos, America, width= largura, color = '#b5ffb9', edgecolor = 'white')
#Plot Europa
plt.bar(grupos, Europa,bottom= America, width= largura, color = '#f9bc86', edgecolor = 'white')
#Plot Japão
plt.bar(grupos, Japao,bottom= [A + B for A, B in zip(America, Europa)], width= largura, color = '#a3acff', edgecolor = 'white')
#Plot Mundo
plt.bar(grupos, Mundo,bottom= [A + B + C for A, B, C in zip(America, Europa, Japao)], width= largura, color = '#d3acfe', edgecolor = 'white')
plt.xticks (grupos, Analise.index)
#plt.xlabel ('Grupo')
plt.ylabel ('Distribuição %')
plt.legend (['América do Norte', 'Europa', 'Japão', 'Mundo'], bbox_to_anchor = (1, -0.1), ncol = 4)

#Grafico 4
plt.subplot(linhas, colunas, 4)
cores = sns.color_palette('hls', 8)
plt.title('Análise por produtora de game (mi)', loc= 'left')
sns.scatterplot(data= data, x= 'Produtora', y= 'Global', color=cores[0])

#Grafico 5
plt.subplot(linhas, colunas, 5)
plt.title('Análise por generos de game (mi)', loc= 'left')
sns.scatterplot(data= data, x= 'Genero', y= 'Global', color=cores[0])

#Grafico 6
plt.subplot(linhas, colunas, 6)
plt.title('Análise por Jogo (mi)', loc= 'left')
sns.scatterplot(data= data, x= 'Jogo', y= 'Global', color=cores[0])

#ajustar layout
plt.subplots_adjust(hspace = 0.35, wspace=0.15)
plt.show()