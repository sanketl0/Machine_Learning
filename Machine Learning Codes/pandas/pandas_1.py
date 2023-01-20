import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s[0])

print("-----------------------")

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s[100])

print("--------")


data = {'a':1, 'b':2, 'c':3}
s = pd.Series(data)
print(s)

print("__________________")

s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s['a'])