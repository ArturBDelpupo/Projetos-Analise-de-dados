import pandas as pd
import matplotlib.pyplot as plt
import numpy
import seaborn as sns
import warnings

data = pd.read_excel('Dados_Empresas_Energia.xlsx')

# print(data.head())
# print (data.describe())
# print (data.shape)

#Series temporais - Setar index

data.set_index('Data', inplace=True)

#print(data.head())

#Grafico
plt.style.use(style='seaborn-v0_8-darkgrid')

#Tamanho
plt.figure(figsize=(13,5))

#Título
plt.title('Análise de ações de energia', loc='left', fontsize = 18 )

#Labels
plt.xlabel('Período')
plt.ylabel('Preço de fechamento - R$')


#Gráfico Petrobrás
plt.plot(data.index, data['Petrobras'], color = '#008c4a', linewidth = 2, alpha = 0.7 ) 
plt.text(data.index [-1], data['Petrobras'].iloc[-1], 'Petrobras', color = '#008c4a' , size = 'large') #[-1] serve para buscar o último nome 

#Plot de todas as outras colunas/Açoes
for coluna in data.columns[1:]:
    plt.plot(data.index, data[coluna], color = "#464646", linewidth = 1, alpha = 0.7 ) 
    plt.text(data.index [-1], data[coluna].iloc[-1], coluna, color = "#464646" )

plt.show()