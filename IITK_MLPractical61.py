import pandas as pd
import numpy as np
# from streamlit import columns

df = pd.DataFrame(np.random.randn(6,4),index = pd.date_range('20190101',periods=6,freq='D') ,
columns = ['A','B','C','D'])
print("\n\n df.A = \n",df.A)
print("\n\ndf['A']=\n",df['A'])
print(df['2019-01-01' : '2019-01-03'])
print(df[0:3])
print("\n\n", df.loc['2019-01-06'])
dates= pd.date_range('20190101', periods=6,freq="D")
print("\n\n",df.loc[dates[0]])
print(df.loc[ : , ['A','D']])
print(df.loc['20190102':'20190106' , ['A','D']])
print(df.loc['20190102' , ['A','D']])
print(df.iloc[3:5,0:2])   ### by interger , slices , acting similiar to numpy and poandas