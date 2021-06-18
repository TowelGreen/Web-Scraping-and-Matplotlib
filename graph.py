import pandas as pd
from matplotlib import pyplot as plt, style
from collections import Counter


data=pd.read_csv('data_scrape.csv')
plt.style.use('fivethirtyeight')


Age=data['Age']
points=data['PTS']


plt.bar(Age,points,color="#008000")
plt.xlabel('Age')
plt.ylabel("Averge Points Per Game")

plt.tight_layout()
plt.show()