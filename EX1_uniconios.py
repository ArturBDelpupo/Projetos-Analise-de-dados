import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

#Baixar o dataset do Kaggle
dw = kagglehub.dataset_download("ramjasmaurya/unicorn-startups")

#print(dw)
#procura o file dentro da pasta onde baixou o dataset
file = os.listdir(dw)

#Ler o arquivo CSV usando pandas
data = pd.read_csv(os.path.join(dw, file[0]))

#print(data.head())  # Exibe as primeiras linhas do DataFrame

#print(data.head())

data['ID'] = range(0, len(data))

#Renomear colunas
data.rename(columns = {
    'Company': 'Empresa',
    'Valuation ($B)': 'Valuation',
    'Date Joined': 'Data de Adesão',
    'Country': 'Pais',
    'City': 'Cidade',
    'Industry': 'Setor',
    'Investors': 'Investidores'
}, inplace= True)

#print(data.columns)  # Exibe os nomes das colunas do DataFrame

#print(data.info()) #Print das informaçoes da base de dados
#print(data.head()) #Print das primeiras informaçoes da tabela
#print (data.isnull().sum()) # Conta quantos dados estao nulos para cada coluna
#print (data.nunique()) #Conta quantos dados são únicos em ada coluna
#print (data['Setor'].unique()) # Mostra todos os dados únicos para a coluna
#print (data['Setor'].value_counts())#Conta quantos valores existe em cada dado unico da coluna desejada
#print (data['Setor'].value_counts(normalize= True))#Porcentagem de cada valor de um total de 100%


'''Print gráfico em barra de maiores setores'''
# plt.bar(x= data['Setor'].value_counts().index, height=data['Setor'].value_counts(normalize= True)) # eixo X = meu index, eixo Y = valor normalizado 
# plt.xticks(rotation = 45, ha = 'right')
# #plt.show()

# plt.clf() #limpa o plt, para nao mostrar o grafico de barra e pizza juntos

'''Print gráfico em pizza de maiores países'''
# #Plot por pais, grafico de pizza (pie)
# analise = data['Pais'].value_counts(normalize=True)*100
# plt.pie (
#     x = analise [0:9],
#     startangle= 90,
#     labels= analise.index[0:9],
#     shadow= True, 
#     autopct= '%1.1f%%'

#     )
# plt.title ('TOP países geradores de unicórnios - Top 10')
# plt.xticks(rotation = 45, ha = 'right')
# print (analise)
# plt.show()

'''Tabela Analítica'''

data['Data de Adesão'] = pd.to_datetime(data['Data de Adesão']) # Transformando a data que era str para datetime
data['Mes'] = pd.DatetimeIndex(data['Data de Adesão']).month #extraindo o mes e salvando em uma nova coluna de dados
data['Ano'] = pd.DatetimeIndex(data['Data de Adesão']).year #extraindo o ano e salvando em uma nova coluna de dados

data['Valuation'] = pd.to_numeric( data['Valuation'].apply( lambda Linha : Linha.replace('$',''))) # transformaçao da coluna valor, retiarndo o $ e transformando para numérico
analise = data.groupby(by = ['Ano', 'Mes', 'Pais', 'Empresa', 'Valuation' ]).count()['ID'].reset_index() #Agrupando a análise pelos parametros ano, mes e pais, contando apenas a coluna ID

analise.loc[
    analise['Pais'] == 'Brazil'
]

#print(analise.loc[analise['Pais'] == 'Brazil'])
analise = data.groupby(by = [ 'Pais' ])['Valuation'].sum().reset_index().sort_values('Valuation', ascending=False)

plt.plot( analise['Pais'][0:15], analise ['Valuation'][0:15])
plt.xticks(rotation = 45, ha = 'right' )
plt.show()