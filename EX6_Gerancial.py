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

print(data.head())


#Relatório -> Report Gerencial

#Tamanho da imagem
fig, ax = plt.subplots(figsize = (15, 8) )

#Parametros para o grid
colunas = 3
linhas = 2

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


#Grafico 2
plt.subplot(linhas, colunas, 2)


#Grafico 3
plt.subplot(linhas, colunas, 3)


#Grafico 4
plt.subplot(linhas, colunas, 4)


#Grafico 5
plt.subplot(linhas, colunas, 5)


#Grafico 6
plt.subplot(linhas, colunas, 6)

#ajustar layout
plt.subplots_adjust(hspace = 0.35, wspace=0.15)
plt.show()