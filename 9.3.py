import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
ab = df[(df.Rok >= 2000) & (df.Rok <= 2005)]
grupa =ab.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.show()