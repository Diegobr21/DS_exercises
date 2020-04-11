import pandas as pd 
import urllib3
import csv

#data = pd.read_csv(r"../datasets/titanic/titanic3.csv") #*sep=",|-. (, default)"
#print(data.head())
list_names=('Clase','A','B','C','D','E','F','G','H','I','J','K','L','M', )
data2 = pd.read_csv(r"../datasets/titanic/titanic3.csv", header=None, names=list_names)
#print(data2.columns.values)

#?Leer desde url

medals_url = 'http://winterolympicsmedals.com/medals.csv'

medals_Data=pd.read_csv(medals_url)
#print(medals_Data.head())

http = urllib3.PoolManager()
r=http.request('GET', medals_url)
response = r.data

resp=response.decode('utf-8')
lines=resp.split('\n')
#print(lines)

with open('Txtprueba.txt', 'w') as fileread:
    for line in lines:
        fileread.write(line)
        fileread.write('\n')
    fileread.close()

dataurl = pd.read_csv(r"Txtprueba.txt")
dataurl.to_excel("prueba.xls")
print(dataurl.head())


#?Leer de XLS/XLSX
filename= "../datasets/titanic/titanic3.xls"
filename2= "../datasets/titanic/titanic3.xlsx"
titanic=pd.read_excel(filename, "titanic3")
titanic2=pd.read_excel(filename2, "titanic3") #nombre de la pestaña


    

