import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings


'''
Data columns (total 8 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   gender                       1000 non-null   str  
 1   race/ethnicity               1000 non-null   str  
 2   parental level of education  1000 non-null   str  
 3   lunch                        1000 non-null   str  
 4   test preparation course      1000 non-null   str  
 5   math score                   1000 non-null   int64
 6   reading score                1000 non-null   int64
 7   writing score                1000 non-null   int64

'''

path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

file = os.listdir(path)

data = pd.read_csv(os.path.join(path, file[0]))

#print (data.head())
#print(data.info())

# print(data['gender'].value_counts(normalize=True)*100)
# print (8 * '==' )
# print(data['race/ethnicity'].value_counts(normalize=True) * 100)
# print (8 * '==' )
# print(data['parental level of education'].value_counts(normalize=True) * 100)
# print (8 * '==' )
# print(data['lunch'].value_counts(normalize=True) * 100) #nao tenho ideia o que é isso
# print (8 * '==' )
# print(data['test preparation course'].value_counts(normalize=True) *100)
# print (8 * '==' )

# plt.subplot(1,3,1)
# sns.boxplot(data = data, y= 'gender', x = 'math score')

# plt.subplot(1,3,2)
# sns.boxplot(data=data, x= 'reading score' , y= 'gender')

# plt.subplot(1,3,3)
# sns.boxplot(data=data, x= 'writing score' , y= 'gender')

#plt.show()

#plt.clf()
print (data.groupby(by = ['gender']).describe()['math score'].reset_index())

# sns.pairplot( data= data, hue= 'gender')
# plt.show()

# sns.boxplot(data=data, x = 'math score', y = 'race/ethnicity')

# sns.boxplot(data=data, x = 'math score', y = 'parental level of education')
# print (data.groupby( by= ['parental level of education']).describe()['math score'].reset_index())

# sns.boxplot(data=data, x = 'math score', y = 'test preparation course')
# print (data.groupby( by= ['test preparation course']).describe()['math score'].reset_index())
# plt.show()

sns.scatterplot(data= data, x='math score', y= 'writing score', hue='gender')
plt.show()