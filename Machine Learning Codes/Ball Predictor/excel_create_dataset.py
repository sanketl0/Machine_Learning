import pandas as pd

df = pd.DataFrame({'Weight':[35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95],
                   'Pattern':['Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth','Rough','Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth','Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth','Rough','Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth'],
                   'Label':['Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket','Tennis','Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket','Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket','Tennis','Tennis','Tennis','Cricket','Tennis','Cricket','Tennis','Cricket']})

writer = pd.ExcelWriter('BallPredictor.xlsx',engine = 'xlsxwriter')
df.to_excel(writer,sheet_name = 'sheet1')
writer.save()