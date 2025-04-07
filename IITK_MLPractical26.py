import numpy as np
res1 = np.random.rand(4)
print("\n res1 = ",res1)
np.random.seed(2)     #### seed values the random numbers predictable & regenratable
res2=np.random.rand(4)    ## virtual random numbers are predictable
print("\n res2 = ", res2)
np.random.seed(0)
res3=np.random.rand(4)
print("\n res3 = ", res3)
np.random.seed(1)
res4=np.random.rand(4)
print("\n res4 = ", res4)