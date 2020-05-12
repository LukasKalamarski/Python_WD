import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

ts = pd.Series(df.Liczba, index=df.Rok)
# funkcja biblioteki Pandas generująca skumulowana sumę kolejnych elementów
ts = ts.cumsum()
ts.plot()
plt.show()