import numpy as np
import pandas as pd
import os
from zlib import crc32
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
housing = pd.read_csv("housing.csv")
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from IPython.display import display
from pandas.plotting import scatter_matrix

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# data 清理 如果有数据的缺失
housing.dropna(subset=["total_bedrooms"])       # 1  放弃这些区域
'''housing.drop("total_bedrooms", axis=1)          # 2 放弃整个区域
median = housing["total_bedroom"].median()      #  3 将缺失值补上为中值（也可为0 或平均值）
housing["total_bedrooms"].fillna(median, inplace=True)'''



