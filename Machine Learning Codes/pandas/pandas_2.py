import pandas as pd 


df = pd.DataFrame({'Data': [11,21,31,41,51,61],'symbol':['a','b','c','d','e','f']})

writer = pd.ExcelWriter('selfpandas.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name='sheet1')

writer.save()

