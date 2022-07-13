import pandas as pd
import numpy as np
data = pd.DataFrame({'one': [100, 99, 88], 'Two': [99, 98, 100]})
data.to_excel(r'E1.xls', sheet_name='Sheet1')
A = pd.read_excel(r'E1.xls', sheet_name='Sheet1', index_col=0)
print(A)

# pip install openpyxl xlrd  xlwt
