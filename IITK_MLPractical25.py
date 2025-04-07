import numpy as np
print("---sum by rows and by column")
x=np.array([[1,2],[3,4]])
print("x=\n",x)
print("x.sum()=",x.sum())
print("x.sum(axis=0) row wise sum = ", x.sum(axis=1) )
print(x[:,0].sum() , x[:,1].sum())
