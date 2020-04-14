import numpy as np 
import pandas as pd
import random

#? Semilla de numeros aleatorios // Seed
np.random.seed(2118)

data = pd.read_csv(r'../../datasets/customer-churn-model/Customer Churn Model.txt')
print('Total Values: ',data.shape)
all_columns = data.columns.values.tolist()

#print(np.random.random())

#genera lista n numeros int aleatorios en rango a-b

def randint(n, a, b):
    randints = []
    for i in range(n):
        randints.append(np.random.randint(a,b))
    return randints

rand_list = randint(15,0,100)
print(rand_list)
np.random.shuffle(rand_list)
print(rand_list)

choice = np.random.choice(all_columns)
print(choice)


