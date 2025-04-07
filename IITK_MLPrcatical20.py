import numpy as np
print(np.all([1,2,3,-4]))  ### all means all number are number but not 0
print(np.all([1,2,3,-4,0]))
print(np.any([1,2,3,4]))
print(np.any([1,2,3,4,4]))   ### any means one number
print(np.any([0,0,0,0.,9]))
print(np.any([0,0,0,0.,0,-1]))
