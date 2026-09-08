import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os


# Download latest version
path = kagglehub.dataset_download("karthickveerakumar/salary-data-simple-linear-regression")

file = os.listdir(path)

data = pd.read_csv(os.path.join(path, file[0]))

#print(data.head())

#Renomear Colunas
data.rename(columns={
    'YearsExperience' : 'Experiencia',
    'Salary' : 'Salario'
}, inplace= True) #Inplace = True serve para renomear na propria base de dados, sem ter que criar uma variável nova

#print(data.head())
#Dimnesão
#print (data.shape)

#Campos nulos
#print(data.isnull().sum())

#print (data.describe())

plt.figure(figsize=(13,5))
plt.title('Análise da renda', fontsize = 14, loc='left')
sns.kdeplot(data= data['Salario'], fill= True)
plt.show()
plt.clf()

plt.title('Análise da experiencia', fontsize = 14, loc='left')
sns.kdeplot(data=data['Experiencia'], fill=True, color='red')

plt.show()