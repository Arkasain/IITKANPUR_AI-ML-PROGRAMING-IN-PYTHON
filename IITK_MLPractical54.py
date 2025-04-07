import  numpy as np
#import the SimpleImputer class
from sklearn.impute import SimpleImputer
#imputer object using the mean strategy and missing_values type for imputation
imputer=SimpleImputer(missing_values=np.nan, strategy='mean')

data=np.array([ [12, np.nan, 34],
              [10, 32, np.nan],
              [np.nan, 11,       20]
           ] )

print("Original Data:\n", data)
imputer=imputer.fit(data)                #fitting the data to the imputer object

data2=imputer.transform(data)
print("\n\nImputed Data: \n", data2)
# ans-the mean and median is taken along the column of the matrix