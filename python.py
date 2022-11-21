
import argparse
import os
import pandas as pd
import sqlalchemy
import pymysql
'''
import pandas as pd
import sqlalchemy
import os
import pymysql
engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
import os
path='/home/user/Documents/python_jupyter/'
getfile=os.listdir(path)
for csvfile in getfile:
    if '.csv' in csvfile:
        df=pd.read_csv(csvfile)
        p=df.to_sql(con=engine, name=csvfile, if_exists='replace',index=False)
        print(p)
'''


# engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
print(engine)
parser=argparse.ArgumentParser()
parser.add_argument('filename')
args=parser.parse_args()

dirpath=args.filename
list_files=os.listdir(dirpath)
for i in list_files:
    path1=dirpath
    if i.endswith('.csv'):
        path1=path1 + '/' + i
        df=pd.read_csv(path1)
        p1=df.to_sql(con=engine, name=i, if_exists='replace',index=False)
        print(p1)


        


















# data = json.load(f)
# print(data)

# import argparse
# import os
# import pandas as pd
# import sqlalchemy
# import pymysql

# engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
# # engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
# parser=argparse.ArgumentParser()
# parser.add_argument('filename')
# args=parser.parse_args()

# dirpath=args.filename
# list_files=os.listdir(dirpath)
# for i in list_files:
#     path1=dirpath
#     if i.endswith('.csv'):
#         path1=path1 + '/' + i
#         df=pd.read_csv(path1)
#         p1=df.to_sql(con=engine, name=i, if_exists='replace',index=False)
#         print(p1)











