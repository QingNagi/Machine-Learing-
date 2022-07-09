import os
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

housing = pd.read_csv("housing.csv")

housing.info()
display(housing.describe())
housing.hist(bins=50, figsize=(20, 15))
plt.show()
display(housing.head())
