import pandas as pd
from glob import glob

stock_files=sorted(glob('start*.csv'))
# print(stock_files)

p=pd.concat((pd.read_csv(file).assign(filename=file) for file in stock_files),ignore_index=True)
p1=pd.DataFrame(p)
# print(p1.head())
p2=p1.to_csv("startups1.csv",index=False)
print(p2)


# print(p.head())