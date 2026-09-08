import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
import plotly.express as px

warnings.filterwarnings('ignore')


data = pd.read_csv('Dados_Incendio.csv', encoding='latin-1')

# print(data.head())
# print(data.shape)
# print(data.describe())

data.rename(columns={
    'year' :'Ano',
    'state' : 'Estado',
    'month' : 'Mes',
    'number' : 'Quantidade',
    'date' : 'Data'
}, inplace= True)

#data.set_index('Data', inplace= True)

#Verificaçao de null ou NA
# print(data.isna().sum())
# print(data.isnull().sum())

#Campos unicos
#print(data.nunique())


#Agrupar por ano
n_queimadas_ano = data.groupby(by=['Ano']).sum()[['Quantidade']].reset_index()
#print(n_queimadas_ano)

plt.figure(figsize= (13,5))
#Estilo
plt.style.use('ggplot')
plt.title ('Total de Incêndios no Brasil: 1997 - 2017', loc = 'left', fontsize = 18)
sns.lineplot(data = n_queimadas_ano, x = 'Ano', y = 'Quantidade', estimator= 'sum')
plt.xlabel ('Periodo')
plt.ylabel ('Quantidade')


#Boxplot por mes
plt.figure(figsize=(13,5))

plt.title ('Incendios por mês', loc='left', fontsize = 18)
n_queimadas_AnoMes = data.groupby(by=['Ano', 'Mes']).sum()[['Quantidade']].reset_index()
sns.boxplot (data=n_queimadas_AnoMes, x = 'Mes', y='Quantidade', palette = 'coolwarm',
             order=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
#plt.show()


#Por estado
plt.figure(figsize=(13,5))
plt.title ('Incendios por estado', loc='left', fontsize = 18)
n_queimadas_estado = data.groupby(by=['Estado']).sum()[['Quantidade']].reset_index().sort_values('Quantidade', ascending=False) #ascending para ordenar a base de dados do maior para o menor 
plt.bar(n_queimadas_estado.Estado , n_queimadas_estado['Quantidade'])
plt.ylabel ('Quantidade')
plt.xticks (rotation = 90)

#Por estado 10 maiores

lista_top10 = n_queimadas_estado['Estado'][0:10].values

analise = 0
plt.figure(figsize=(13,5))
for coluna in lista_top10:
    filtro = data.loc[data['Estado'] == coluna]
    analise_top10 = filtro.groupby(by=['Ano'])['Quantidade'].sum().reset_index()

    sns.lineplot(data=analise_top10, x='Ano', y='Quantidade', label=coluna)


plt.ylabel('Quantidade')
plt.xlabel('Ano')
plt.legend(lista_top10, bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()



# Plot Geográfico
# Gerando os estados
Estados = n_queimadas_estado.sort_values('Estado')['Estado'].values
# Gerando os valores
Valores = n_queimadas_estado.sort_values('Estado')['Quantidade'].values
# Latitudes
Lat = [ -8.77, -9.71,	1.41, -3.07,	-12.96, -3.71, -15.83, -19.19, -16.64, -2.55,	-12.64,	
       -18.10, -7.06, -5.53, -8.28, -8.28,	-22.84,	-11.22,	1.89,	-27.33,	-23.55,	-10.90,	-10.25 ]
# Longitudes
Log = [ -70.55,	-35.73,	-51.77,	-61.66,	-38.51,	-38.54,	-47.86,	-40.34,	-49.31,	-44.30,	-55.42,	-44.38,	
       -35.55,	-52.29,	-35.07,	-43.68,	-43.15,	-62.80,	-61.22,	-49.44,	-46.64,	-37.07,	-48.25 ]
# Organizados os dados
Dicionario = {
    'Estados' : Estados,
    'Latitude' : Lat,
    'Longitude' : Log,
    'Incêndios' : Valores
}

# Lendo o dicionario
Analise_Geografica = pd.DataFrame ( Dicionario )

# Mapa Geografico
fig = px.density_map(
    Analise_Geografica,
    lat='Latitude',
    lon='Longitude',
    z='Incêndios',
    radius=30,
    center=dict(lat=-12.700, lon=-46.5555),
    zoom=3,
    map_style='open-street-map',

)

fig.update_layout(coloraxis_showscale=False)
fig.show()
#plt.show()

