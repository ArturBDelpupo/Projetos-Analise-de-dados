import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as Dash


data = pd.read_excel('Dados_Bitcoin.xlsx')

# print (data.head())
# print (data.describe())
# print (data.shape)

#Set index
data.set_index('Date', inplace=True)

#Gráfico de linhas
#fig = px.line(data, y = 'Close')

media_movel = data ['Close'].rolling(5).mean()
media_tendencia = data['Close'].rolling(30).mean()

#Criar Dashboard (customizavel)
figure = Dash.Figure()

figure.add_trace(
    Dash.Scatter(
        x= data.index,
        y= data['Close'],
        mode= 'lines',
        name= 'Fechamento',
        marker_color= "#f69a49"

    )
)
#Adicionando média móvel
figure.add_trace(
    Dash.Scatter(
        x= data.index,
        y= media_movel,
        mode= 'lines',
        name= 'Média móvel',
        marker_color= "#5f0202"

    )
)

#Adicionando tendencia
figure.add_trace(
    Dash.Scatter(
        x= data.index,
        y= media_tendencia,
        mode= 'lines',
        name= 'Tendência',
        marker_color= "#007f39"

    )
)

figure.update_layout(
    #título
    title = 'Análise do bitcoin 2017-2022',
    #Tamanho
    font=dict(size=20),

    #Eixos
    xaxis=dict(
        title=dict(
            text='Período Histórico', 
            font=dict(size=14),
        ),
        tickfont=dict(size=10)
    ),
    yaxis=dict(
        title=dict(
            text= 'Preço do Fechamento ($)',
            font=dict(size = 14)
        ),
        tickfont=dict(size=10)
    ),
    
    

)
figure.show()