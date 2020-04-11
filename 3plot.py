import pandas as pd 
import csv
import matplotlib.pyplot as plt

data = pd.read_csv(r"../../datasets/customer-churn-model/Customer Churn Model.txt")
#print(data.head())
#savefig('path_whereimg_save.jpeg')

#?Scatter Plot

print(data.plot(kind='scatter', x='Day Mins', y='Day Charge'))
figure, axes = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind='scatter', x='Day Mins', y='Day Charge',ax= axes[0][0])
data.plot(kind='scatter', x='Night Mins', y='Night Charge', ax=axes[0][1])
data.plot(kind='scatter', x='Day Calls', y='Day Charge',ax= axes[1][0])
data.plot(kind='scatter', x='Night Calls', y='Night Charge', ax=axes[1][1])