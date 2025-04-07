#dropping rows with at least 1 null value
import pandas as pd
import numpy as np
from numba.cuda.nvvmutils import declare_atomic_add_float64

dict={'First score': [100,   np.nan,  np.nan,    95],
      'Second score': [ 30,  np.nan,   45,   56],
      'Third score ': [ 52,  np.nan,   80,     98],
      'Fourth score': [60,67,     68,65]
      }
#creating a dataframe from dictionary
df=pd.DataFrame(dict)
print(df)
df6=df.dropna(axis=1)   ### delete the column
print("df6=\n", df6)