import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy 
import os
import warnings
import plotly.graph_objects as go

'''
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   Data        247 non-null    datetime64[us]
 1   Maior       247 non-null    float64       
 2   Menor       247 non-null    float64       
 3   Abertura    247 non-null    float64       
 4   Fechamento  247 non-null    float64       
 5   Volume      247 non-null    int64         
 6   Adj Close   247 non-null    float64       
dtypes: datetime64[us](1), float64(5), int64(1)

'''

warnings.filterwarnings('ignore')

data = pd.read_excel('Vase_004 - Magalu.xlsx')

#print(data.shape())
#print(data.info())
#print (data.describe())

#Séries Temporais

#Mudando index da tabela
dados = data.set_index('Data')

# plt.figure( figsize= (13,5))

# sns.set_theme(style="darkgrid")
# plt.title ('Análise das ações Magalu - Fechamento', fontsize = 14, loc= 'left')
# plt.plot(dados.index, dados ['Fechamento'] )
# plt.xlabel ('Período da cotação')
# plt.ylabel('Valor da Ação (R$)')
# plt.show()

# print (dados.tail()) 

fechamento = dados ['Fechamento'].rolling(window= 5).mean() #média móvel de 5 dias (window = 5)
tendencia = dados['Fechamento'].rolling (window=30).mean()

plt.figure( figsize= (13,5))
plt.plot(dados.index, dados ['Fechamento'])
plt.plot(fechamento.index, fechamento)
plt.plot(tendencia.index, tendencia)
plt.legend()
plt.show()
print (fechamento)

#Boxplot mensal
dados ['Mes'] = dados.index.month
plt.figure(figsize= (13,5))
sns.boxplot(y = dados ['Fechamento'], x = dados['Mes'] )
plt.show()

analise_mes = dados.groupby([dados['Mes']]).describe()['Fechamento']
print (analise_mes)

#Grafico  

grafico = go.Figure(
    data = [go.Candlestick(x = dados.index, 
                        open = dados['Abertura'],
                        high = dados['Maior'],
                        low = dados['Menor'],
                        close = dados['Fechamento'])] 
)

grafico.update_layout(xaxis_rangeslider_visible = False)
grafico.show()