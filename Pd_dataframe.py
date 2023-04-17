# from api import result
from matplotlib import pyplot as plt
import pandas as pd
from IPython.display import display # pip install IPython
import jinja2 as jinja # pip install Jinja2
# pip install pandas
global x
global y
global year
year = []
x = []
y = []

skip_rows = []
for i in range(2,20):
    skip_rows.append(i)

data = pd.read_csv('data.csv', sep='[;]', header=0, usecols=["KOMK", "TID", "INDHOLD"], engine='python', skiprows=skip_rows, nrows=20)
# komk = data['KOMK']
# print(data)
# data.replace(',','.')
x = data['KOMK'].values.tolist()
y = data['INDHOLD'].values.tolist()

for index,item in enumerate(y):
    # print(item)
    y[index] = float(y[index].replace(',','.'))

# print('x: ',x)
# print('y: ',y)

f = pd.DataFrame(data)


display(f)

f.style # virker ik