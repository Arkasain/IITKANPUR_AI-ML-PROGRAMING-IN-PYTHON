import pandas as pd
import numpy as np
from xarray.core.missing import bfill

dict={'first score':[100,90,np.nan,95],
      'second score':[30,45,56,np.nan],
      'third score':[np.nan,40,80,98]}
#creating data frame from list
df=pd.DataFrame(dict)
print(df)
#using isnull()
df2=df.fillna(method='bfill')
print(df2)