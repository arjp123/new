import argparse
import os
import pandas as pd
import sqlalchemy
import pymysql

engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
print(engine)
# engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')
parser=argparse.ArgumentParser()
parser.add_argument('filename')
args=parser.parse_args()

dirpath=args.filename
# print(dirpath)

list_files=os.listdir(dirpath)
for i in list_files:
    path1=dirpath
    if i.endswith('.csv'):
        path1=path1 + '/' + i
        df=pd.read_csv(path1)
        p1=df.to_sql(con=engine, name=i, if_exists='replace',index=False)
        print(p1)









