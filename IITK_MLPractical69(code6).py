#Binarize Data (Make Binary)
#-----------------------------
import numpy as np
from sklearn.preprocessing import Binarizer

X = np.array( [ [ 1., -1., 2.],
[ 2., 0., 0.],
[ 0., 1., -1.] ] )

#Default Threshold value is 0
transformer = Binarizer(threshold=1)
data2 = transformer.transform(X)

print( data2 )

#You can transform your data using a binary threshold.

# All values above the threshold are marked 1 and
# all equal to or below are marked as 0.

# This is called binarizing your data or  thresholding your data.

# It can be useful when you have probabilities that you want to make crisp values.

# It is also useful when feature engineering and you want to add new features that indicate something meaningful.


