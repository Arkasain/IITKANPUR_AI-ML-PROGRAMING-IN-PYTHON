import pandas as pd
import  numpy as np
dict = {'first score':[100,90,np.nan,95],
        'Seconf score':[30,45,56,np.nan],
        'Third score':[np.nan,40,80,98]
        }
## creating datframe from list
df=pd.DataFrame(dict)
##using isnull() function
df2=df.isnull()
print(df2)              