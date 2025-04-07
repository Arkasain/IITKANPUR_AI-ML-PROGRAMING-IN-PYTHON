import pandas as pd
import numpy as np
# from streamlit import columns

df = pd.DataFrame(np.random.randn(6,4),index = pd.date_range('20190101',periods=6,freq='D') ,
columns = ['A','B','C','D'])
print("\n\n Pandas dataframe = \n",df)
print("\n\n headings dataframe = \n",df.columns)
print("\n\n Row headiong dataframe = \n",df.index)
print("\n\n values dataframe = \n",df.values)
print("\n",df.columns[2:4])
print("\n\n")
print(df.groupby('E').size())