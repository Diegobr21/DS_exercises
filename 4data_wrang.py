import pandas as pd

data = pd.read_csv(r'../../datasets/customer-churn-model/Customer Churn Model.txt')
print('Total Values: ',data.shape)

#data['column'].values.ravel().sum() get a sum of all values in that column
#? Crear un subconjunto de datos

#Work with the smallest subset possible

acc_len = data['Account Length'] #1 columna

subset = data[['Account Length', 'Day Calls', 'Eve Charge']]

#print(acc_len.head())
#print(subset.head())
# print(type(subset)) Type: DataFrame

desired_columns = ['Account Length', 'Day Calls', 'Night Calls']

not_desired = ['Phone', 'Eve Mins', 'Eve Charge', 'Account Length', 'Area Code']

all_columns = data.columns.values.tolist()
print(f'All cloumns: {all_columns} \n')

only_desired = [x for x in all_columns if x not in not_desired]

"""
or you can do:
a = set(desired_columns)
b = set(all_columns)
sublist = b-a
sublist = list(sublist)

"""

#print(data[only_desired].head())
data_D = data[only_desired]
#subset2 = data[desired_columns]
#print(subset2.head())
#?Slicing
#print(data[100:120])

#*Restricción de valores

#Usuarios con 'Area Code' == 415, o algun otro campo que cumpla con la condición

data1 = data[data['Area Code'] == 408]
data2 = data[data['Night Mins'] > 310]
datany = data[(data['State'] == 'NY') & (data['CustServ Calls'] != 0) ]
dataor = data[(data['CustServ Calls'] > 2) | (data['Night Mins'] > 300) | (data['Day Mins'] > 300)  ]
data_diurnos = data[(data['Day Mins']) > (data['Night Mins'])]
data_nocturnos = data[(data['Day Mins']) < (data['Night Mins'])]

#print(data1)
print('NightMins > 310: ',data2.shape)
print('NY with CustCalls: ',datany.shape)
print('NightMins or DayMins > 300 or CustCalls > 2',dataor.shape)
print('Diurnos: ',data_diurnos.shape)
print('Nocturnos: ',data_nocturnos.shape)

#* columna y fila a la vez
#[columnas][filas]
subset_100 = data[['Day Mins', 'Night Mins', 'State']][:100]
print('Primeros 100 solo minutos y estado',subset_100.shape)

#*.iloc(position) y .loc(label)
#[[filas], [columnas]]
print('loc e iloc')
iloc = data.iloc[:10, [2,5,9]] #primeras 10 filas de las columnas 2,5,9
print(iloc.head())
loc = data.loc[100:201, ['State', 'Day Mins', 'Day Charge']]
print(loc.head())

#*Crear nueva columna a partir de otra(s)
data['Total Mins'] = data['Day Mins'] + data['Eve Mins'] + data['Night Mins']
data['Total Charge'] = data['Day Charge'] + data['Eve Charge'] + data['Night Charge']

loc = data.loc[100:201, ['State', 'Total Mins', 'Total Charge']]
print('\n',loc.head())