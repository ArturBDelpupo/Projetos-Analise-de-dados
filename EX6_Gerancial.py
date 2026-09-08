import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
import os
import numpy
import kagglehub

path = kagglehub.dataset_download("sidtwr/videogames-sales-dataset")

file = os.listdir(path)

data = pd.read_csv(os.path.join(path, file[0]), encoding='latin-1')

print(data.head())