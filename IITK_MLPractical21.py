## types of operation broadcasting
## scaler operation broadcasting [single value applied on every arrray ]
## Array operation broadcasting  [operation perform are applied in every single indevisual array]

import numpy as np
n1=np.array([4,5,6])
n2 = np.array([1,2,3])
print("n1 = ",n1 )
print("n2 = ",n2 )
print("n1+n2 = ",n1+n2 )
print("n1-n2 =", n1-n2)
n3 = np.array([4,5,6,7])
print(n1+n3)