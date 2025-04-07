#dropping rows with at least 1 null value
import pandas as pd
import numpy as np
from numba.cuda.nvvmutils import declare_atomic_add_float64

dict={'First score': [100,   90,  np.nan,    95, np.nan],
      'Second score': [ 30,  np.nan,   45,   56, np.nan],
      'Third score ': [ 52,    40,   80,     98, np.nan],
      'Fourth score': [np.nan,np.nan,np.nan, 65, np.nan]
      }
#creating a dataframe from dictionary
df=pd.DataFrame(dict)
print(df)

#drop all row that have any NaN values
df2=df.dropna()
print('\n\n', df2)

# drop only if all columns are NaN
df3=df.dropna(how='all')
print("df3=\n", df3)

#drop row if it does not have at least three values that are not NaN
df4=df.dropna(thresh=3)
print("df4=\n",df4)

# Drop only if NaN in specific column (as asked in the question
df5=df.dropna(subset=['Second score'])
print("df5=\n", df5)

# Using dropna() function with axis=1 for column wise deletion
df6=df.dropna(axis=1)
print("df6=\n", df6)