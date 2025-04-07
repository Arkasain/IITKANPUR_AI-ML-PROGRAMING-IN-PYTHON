#### BOOLEAN INDEXING #####


import pandas as pd
import numpy as np
# from streamlit import columns

df = pd.DataFrame(np.random.randn(6,4),index = pd.date_range('20190101',periods=6,freq='D') ,
columns = ['A','B','C','D'])
print("\n\n df = \n",df)
print("\n\ndf['A']=\n",df['A'])
print("\n\n df.A >0 = \n", df.A >0)
print("\n\n",df[(df.B<0) & (df.D<0)])
print("\n", df[df.B > df.B.mean()])
print("\n",df['B'][df.B>df.B.mean])
