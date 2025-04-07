import pandas as pd
import numpy as np
# from streamlit import columns

df = pd.DataFrame(np.random.randn(6,4),index = pd.date_range('20190101',periods=6,freq='D') ,
columns = ['A','B','C','D'])

print("\n\n pandas datframe =\n",df)
print("\n\n sorted values :\n",)
print(df.sort_values(by='B',ascending=True))