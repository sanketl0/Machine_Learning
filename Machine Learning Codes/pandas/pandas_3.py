import pandas as pd

file  = 'Marvellous.xlsx'
batch = pd.read_excel(file)

print(batch.head())

batch_sheet1 = pd.read_excel(file, sheet_name=0 , index_col= 0)
print(batch_sheet1.head())