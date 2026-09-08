import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


data = pd.read_excel('Dados_Pib.xlsx')

print(data.head())
print(data.describe)

print (data.groupby(by=['Territorialidades', 'Ano']).mean())