import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


data = pd.read_excel('Dados_Pib.xlsx')

print(data.head())
print(data.describe)

#print (data.groupby(by=['Territorialidades', 'Ano']).mean())

#Sistema de grids
fundo = '#f5f5f5'

#Criar sistema de grids
grid_graf = sns.FacetGrid(data, col='Territorialidades', hue='Territorialidades', col_wrap= 4)
#Adiciona um grafico de linha a cada mini gráfico
grid_graf = grid_graf.map(plt.plot, 'Ano', 'PIB per capita')
#Adicionar sombra para gráficos + ajute de titulo
grid_graf = grid_graf.map(plt.fill_between, 'Ano', 'PIB per capita', alpha = 0.2).set_titles('{col_name}') #Set_titles modificou o padrao de titulo, colocando o estado primeiro

#adcionar subtitulos
grid_graf.figure.suptitle ('Evolução da Renda per capita por Estado')
Rodape = '''Essse relatório foi elaborado no treinado "Python para Análise de Dados"
Está dispónivel no canal do youtube @Data Viking',
by: @Artur Delpupo || github : https://github.com/ArturBDelpupo
    '''
grid_graf.figure.text( 0.3, -0.002, Rodape, fontsize= 8 )

grid_graf.figure.subplots_adjust(top=0.93, bottom=0.12, hspace=0.45, wspace=0.2)

plt.show()
