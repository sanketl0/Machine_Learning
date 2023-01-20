import pandas as pd
import matplotlib.pyplot as plt

file = 'Marvellous_m.xlsx'
data = pd.read_excel(file)

print("All data from excel file:")
print(data)

print("first five rows from file:")
print(data.head())

print("first four rows from file:")
print(data.head(4))

print("laat five rows from file:")
print(data.tail(3))

print(data.shape)

sort_data = data.sort_values(['Name'],ascending=False)
print("sorted data:")
print(sort_data)

data['Age'].plot(kind="hist")
plt.savefig('fig_3.jpg')
plt.show()

data["Age"].plot(kind="barh")
plt.savefig('fig_4.jpg')
plt.show()

