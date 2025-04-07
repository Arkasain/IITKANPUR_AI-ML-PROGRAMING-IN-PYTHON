### filling null value with a single value


import pandas as pd
import  numpy as np
dict = {'first score':[100,90,np.nan,95],
        'Seconf score':[30,45,56,np.nan],
        'Third score':[np.nan,40,80,98]
        }
## creating datframe from list
df=pd.DataFrame(dict)

df2=df.fillna(method='pad') ### previous value are add next ....
print(df)
print()
print(df2)