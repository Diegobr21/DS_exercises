import pandas as pd 
import urllib3
import csv

data = pd.read_csv(r"../datasets/titanic/titanic3.csv")
#print(data.head(10))
print(data.shape)
#print(data.tail)

#!Resumen de estadisticos básicos
print(data.describe())
print(data.dtypes)

#?Contar Valores faltantes
nulls = pd.isnull(data["body"]).values.ravel().sum()
print(nulls)

#!Borrar las filas con valores faltantes
#data.dropna(axis=0, how='all') #axis = 0-fila 1-columna
#data.dropna(axis=0, how='any')#axis = 0-fila 1-columna, how=all/any/

#!Reemplazar los valores faltantes
data2 = data
data2 = data2.fillna(0) #*Rellenar con 0
data3 = data
data3 = data3.fillna('Desconocido')
data4 = data
data4['body'] = data4['body'].fillna(0)
data4['home.dest'] = data4['home.dest'].fillna('Desconocido')

#*Sustituir los valores faltantes por el promedio de los existentes
nulls2 = pd.isnull(data['age']).values.ravel().sum()
data4['age'] = data4['age'].fillna(data4['age'].mean())
#print(data4.head(15))

#*Sustituir por un valor conocido adelante o atras
data5=data
data5['age'].fillna(method='ffill')
data5['age'].fillna(method='backfill')

#!Dummy Variables
dummy_sex = pd.get_dummies(data['sex'], prefix='sex')
print(dummy_sex.head(15))
data = data.drop(['sex'], axis=1) #Sin columna sex
data = pd.concat([data, dummy_sex], axis=1) #Concatenamos las nuveas 2 comlumnas
print(data.head())

def createDummies(df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = df.drop([var_name], axis=1)
    df = pd.concat([df, dummy], axis=1)
    return df

print(createDummies(data2, 'sex'))