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
<<<<<<< HEAD
from pandas.plotting import scatter_matrix
=======
>>>>>>> 9581f5bdf70009e6f13abc057161653c57d02f91

#def split_train_test(data, test_ratio):
#   shuffled_indices = np.random.permutation(len(data))
#    test_set_size = int(len(data) * test_ratio)
#    test_indices = shuffled_indices[:test_set_size]
#    train_indices = shuffled_indices[test_set_size:]
#    return data.iloc[train_indices], data.iloc[test_indices]

#train_set, test_set = split_train_test(housing, 0.2)


'''def test_set_check(identifier, test_radio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_radio * 2**32


def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

print(len(train_set))
print(len(test_set)) '''

'''train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(len(train_set))
print(len(test_set))

housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 5.4, 6., np.inf], labels=[1, 2, 3, 4, 5])
housing["income_cat"].hist()
print(housing["income_cat"])
split = StratifiedShuffleSplit(n_splits=1, train_size=0.2, random_state=42)

for train_index,test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

print(strat_train_set["income_cat"].value_counts() / len(strat_test_set))'''

'''housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, s=housing["population"]/100, label="population",
             figsize=(10,7), c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)
plt.legend()'''

corr_matrix = housing.corr()
<<<<<<< HEAD
display(corr_matrix["median_house_value"].sort_values(ascending=False))     # 寻找相关系数 （皮尔逊r）


attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))


housing.plot(kind='scatter', x='median_income', y='median_house_value', alpha=0.1)
plt.show()



=======
display(corr_matrix["median_house_value"].sort_values(ascending=False))
plt.show()
>>>>>>> 9581f5bdf70009e6f13abc057161653c57d02f91
