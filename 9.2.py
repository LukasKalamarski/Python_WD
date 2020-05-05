import pandas as pd
import numpy as np
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
# print(df[(df.Liczba > 1000)])
# print(df[(df.Imie == 'ŁUKASZ')])
# ab = df[(df.Rok >= 2000) & (df.Rok <= 2005)]
# ac = ab.groupby(['Rok']).agg({'Rok':['sum']})
# print(ac)
# print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
print(df.groupby(['Imie']).agg({'Liczba':['sum']}))