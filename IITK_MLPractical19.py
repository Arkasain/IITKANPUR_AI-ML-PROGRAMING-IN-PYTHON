import numpy as np
arr = np.array([11,22,-33,0,44,55])
print("arr.sum()=",arr.sum())
print(np.sum(arr))     ## this is universial function`
print("arr.std()=",arr.std())
print("arr.mean()=",arr.mean())
print("np.mean(arr)=",np.mean(arr))
print("arr.max()=",arr.max())
print("arr.min()=",arr.min())
print("arr.size=",arr.size)
print("arr.shape()=",arr.shape)
print("arr.dtype()=",arr.dtype)
### following line will print(index of nonzero values)
print("arr.nonzero()=",arr.nonzero())