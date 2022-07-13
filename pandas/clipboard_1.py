import pandas as pd
import sqlite3
import pymongo
from pymongo.mongo_client import MongoClient
data = pd.DataFrame({'one': [100, 99, 88], 'Two': [99, 98, 100]})

data.to_clipboard(sep=',')    # 写入粘贴板
print(pd.read_clipboard(sep=','))

data.to_pickle('dummy.pkl')
f2 = pd.read_pickle('dummy.pkl')
print(f2)

data.to_hdf('F1.h5', key='f1')
data3 = pd.read_hdf('F1.h5')
print(data3)

# install tables
conn = sqlite3.connect('First.bd')   # 建立和连接数据库
data.to_sql('test', conn, if_exists='replace')    # 写入test表中
conn.close()  # 关闭连接

'''conn = sqlite3.connect('First.db')  # 连接数据库
sql = 'Select * from test'    # sql语言
d2 = pd.read_sql('Select * from test', conn, index_col='index')  # 读取sql
conn.close()
print(d2)'''

conn = MongoClient('localhost', port=27017)
c1 = conn.db.F1
# c1.remove()
t1 = data.to_dict(orient='list')
print(t1)
c1.insert_many([t1])

d1 = c1.find({'_id': False})[0]
print(d1)
e1 = pd.DataFrame(d1)
print(e1)