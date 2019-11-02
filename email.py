import pandas as pd

mails = pd.ExcelFile('mails.xlsx')
sheet = mails.parse('Export Worksheet')

names = pd.Series(sheet['CH_FULL_NAME'])
emails = pd.Series(sheet['CH_EMAIL'])

for i in range(len(names)):
    print(names[i],"   ",emails[i])
