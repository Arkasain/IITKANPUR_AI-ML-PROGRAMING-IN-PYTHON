import  numpy as np
ddarr = np.array( [[1,2,3],[4,5,6]])
print("ddarr.ndim = ", ddarr.ndim)    ##ddarr.ndim=2
print("ddarr.shape = ", ddarr.shape)   ##ddarr.shape=(2,3)
print("ddarr.size = ", ddarr.size)    ##ddarr.size=6
print("len(ddarr) = ", len(ddarr))
print("ddarr.dtype = ", ddarr.dtype)
##ddarr.dtype = int32
print(ddarr)
print("ddarr[0,1] = ", ddarr[0,1])
print("ddarr[0] = ", ddarr[0])
print("ddarr[:,0] = ", ddarr[:,2])
print("ddarr[0:1,] = ", ddarr[0:1, ])

