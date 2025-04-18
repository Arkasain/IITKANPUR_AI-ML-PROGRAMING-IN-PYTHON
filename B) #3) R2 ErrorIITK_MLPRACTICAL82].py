#B.3) Example of evaluating an algorithm by R Squared.
#----------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                  'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

dataframe = pd.read_csv(filename, names=names)

array = dataframe.values
X = array[:,0:13]
Y = array[:,13]

kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LinearRegression()

scoringMethod = "r2"
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod )

print("R2: %.3f" % ( results.mean( ) ) )