import pandas as pd
import sqlalchemy
import pymysql
engine=sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/db1')

df=pd.read_csv("friends.csv")
friends1=df




# df=pd.read_sql("startups",engine)
print(df)

# Import dataframe into MySQL
import sqlalchemy
'''
# database_username = 'ENTER USERNAME'
# database_password = 'ENTER USERNAME PASSWORD'
# database_ip       = 'ENTER DATABASE IP'
# database_name     = 'ENTER DATABASE NAME'
# database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
#                                                format(database_username, database_password, 
#                                                       database_ip, database_name))
'''




# p=df.to_sql(con=engine, name='friends', if_exists='replace',index=False)
# print(p)

# import os
# import glob
# path="../Documents/"
# l=os.listdir(path)
# print(l)
# g=glob.glob('*.csv')
# for i in g:
#     print(i)







import os
path='/home/user/Documents'
p=os.listdir(path)
# print(p)

for i in p:
    if '.txt' in i:
        print(i)

