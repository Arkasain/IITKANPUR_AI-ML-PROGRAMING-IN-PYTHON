#1) Rescale data (custome range between 1 and 10)
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

filename = ('indians-diabetes.data.csv')
hnames=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# 0 1 2 3 4 5 6 7 8
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
# separate array into input and output components
X = array[ : , 0:8] # [ row , cols ]
Y = array[ : , 8]
scaler = MinMaxScaler( feature_range=(1,10) ) #Range

#First Method
rescaledX = scaler.fit_transform(X)

#Second Method
scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
print( rescaledX [ 0:30 , : ] ) # [ row , cols ]


#Step-1
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
#In Simple way,
# X_std = X - min(X) / max(X) - min(X)

#Step-2
# X_scaled = X_std * (max - min) + min