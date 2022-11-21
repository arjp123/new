
import argparse
import os
import pandas as pd
import sqlalchemy
import pymysql
import json
from jsonargparse import ActionPathList
import mysql.connector 
import pymysql# print(data['host'])
import os

from os import path
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("fullreport",help="printing the full report",default="*")
args = parser.parse_args()

pol=args.fullreport

poly=pol[1:]

from os import path



def parts(poly):
    ret = []
    head, tail = path.split(poly)
    if tail != '':
        ret.append(tail)
    while head != '':
        head, tail = path.split(head)
        ret.append(tail)
    return ret[::-1]

ret = path.join(*parts(poly)[:-1])
ret='/'+ret





with open(pol) as file:
    data = json.load(file)




engine=sqlalchemy.create_engine('mysql+pymysql://'+data['user']+':'+data['password']+'@'+data['host']+':3306/'+data['database'])



dirpath=ret
list_files=os.listdir(dirpath)

for i in list_files:
    path1=dirpath
    if i.endswith('.csv'):
        path1=path1 + '/' + i
        df=pd.read_csv(path1)
        names=i[:i.index(".")]
        p1=df.to_sql(con=engine,name=names, if_exists='replace',index=False)
        print(p1)


        




    


