import numpy as np
import pandas as pd


dict1={"name":["arjun","polard","kio"],
       "marks":[90,89,78],
       "city":["jaipur","pune","udaipur"]
}


df=pd.DataFrame(dict1)
p1=df.to_csv('sohail.csv')
print(p1)  # read dict 

# import pandas as pd

# emp_data = {"Name": ["Alex Doe", "Bob Colly", "Cynthia Mike", "Doreen James"],
# "Airtime ($)": [100 ,250, 400, 1000],
# "Salary ($)": [35000, 45000, 52000, 60000],
# "Location": ["Nairobi", "New York", "Hong Kong", "Berlin"]
# }
# df = pd.DataFrame(emp_data)
# print(df)



# df=df.to_csv("friends.csv")
# print(df)


# df=df.to_csv("friends.csv",index=False)                    # index nahi save hoga
# print(df)

# df=df.head(5)
# print(df)

# df=df.tail(2)
# print(df)




# df=df.describe()
# print(df)


# df1=pd.read_csv("startup.csv")
# print(df1)

# df1=pd.read_csv("../python_jupyter/startup.csv")
# print(df1)

# print(df1['Sr_No'][1])

# df1['Sr_No'][1]=103   # update




# df1=df1.to_csv("harry.csv")
# print(df1)

# df1.index=['first','second']
# print(df1)


df.index=["first","second","third"]
# print(df)

df['name']['second']="KALA"
# print(df)





# print(df.head(4))
# print(df1.head(4))

#              -                    -------------------   
ser=pd.Series(np.random.rand(34))
# print(ser)
# print(type(ser))

newdf=pd.DataFrame(np.random.rand(345,5) , index=np.arange(345))
# print(newdf)

# ser=pd.DataFrame(np.random.rand(34))
# print(ser)
newdf1=pd.DataFrame(np.random.rand(345,5))
# print(newdf1)

newdf=newdf.head()

p=newdf.describe()
print(p)

p1=newdf.dtypes
# print(p1)






newdf[0][1]="harry"
# print(newdf)

# print(newdf.dtypes)

# print(newdf.index)


# print(newdf.columns)




newdf=newdf.to_numpy()
# print(newdf)


newdf[1][0]= 0,527
# print(newdf)
# print(type(newdf))




# newdf=newdf.T         #  ------------- Transpose row column me convert ho gaya or column row me ex (3 X 5) then (5 X 3)
# print(newdf[0][1])



# print(newdf)

# print(type(newdf))

# np.sort_index(newdf, axis=1 , ascending=False)
# print(newdf)

# newdf.head(7)
# print(newdf)

# print(newdf)


newdf=pd.DataFrame(np.random.rand(34,5))
# print(newdf.head())
# print(type(newdf))

newdf=newdf.sort_index(axis=1, ascending=False)
# print(newdf.head())

newdf=newdf.sort_index(axis=0, ascending=False)
# print(newdf.head())

# axis=0 mean row and axis=1 mean columns


newdf=newdf.sort_index(axis=0)
# print(newdf.head())


# print(type(newdf[0]))
# print(type(newdf))


n=newdf  #    view , if we do any changes in n then it's automatically update on newdf
n[0][0]=91919
# print(newdf.head())

# n2=newdf.copy()
# n2[4][0]=111111
# print(n2.head())

# print(newdf.head(5))

newdf.loc[0,0]=88
# print(newdf.head())


newdf.columns=list("ABCDE")

newdf.loc[0,"E"]=77
# print(newdf.head())
# newdf=newdf.to_numpy()

# newdf=pd.DataFrame(np.random.rand(300,5))
# newdf=newdf.loc[[1,2],['C','D']]
# print(newdf)



# newdf=newdf.loc[[1,2],['C','D']]
# print(newdf)


# newdf=newdf.loc[:,['C','D']]   # 
# print(newdf)

# print(newdf.head())
# newdf=newdf.loc[[1,2],:]  #  starting loc[row,column]  1,2 mean row or : all columns 
# print(newdf)


# newdf=newdf.loc[(newdf['A']<0.3)]
# print(newdf)



# newdf=newdf.loc[(newdf['A']<0.3) & (newdf['E']<0.7)]
# print(newdf)


# newdf=newdf.iloc[[0,1],[0,1]]
# print(newdf)



print(newdf.head())
# newdf=newdf.drop(0)          # 0 mean row ko drop kardega
# print(newdf.head())

# newdf=newdf.drop(['A','C'],axis=1)  # axis=1 for column A,C remove
# print(newdf.head())

# newdf=newdf.drop([0,1],axis=0)  # axis=0 mean for row 0,1 remove
# print(newdf.head())




# print(newdf.head())  # inplace = True mean jobi delete hua he woh permanet delete ho jaye

newdfs=newdf.copy()
# new_df=newdf.drop(['A','C'],axis=1,inplace=True)
print(newdf.head())



