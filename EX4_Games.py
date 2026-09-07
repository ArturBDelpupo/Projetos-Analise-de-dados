import kagglehub
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Download latest version
path = kagglehub.dataset_download("sidtwr/videogames-sales-dataset")

file = os.listdir(path)

data = pd.read_csv(os.path.join(path, file[0]), encoding='iso-8859-1')

print(data.shape)
#print(data.head())

#print (data.isnull().sum())

data = data.dropna()

print(data.describe())