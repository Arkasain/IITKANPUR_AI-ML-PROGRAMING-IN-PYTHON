# A.3) Logistic Regression Performance Metrics : Area Under ROC Curve.
#-------------------------------------------------------------------------------------
#Receiver Operating Characteristic Area Under the Curves
#Area under ROC Curve (or AUC for short) is a performance metric for binary classification problems.
# The AUC represents the ability of a model to discriminate between positive and negative classes.
# An area of 1.0 represents a model that made all predictions perfectly.
# An area of 0.5 represents a model that is as good as random.
# ROC can be broken down into sensitivity and specificity.
# A binary classification problem is really a trade-off between sensitivity and specificity.
#Sensitivity is the true positive rate also called the recall.
# It is the number of instances from the positive (first) class that actually predicted correctly.
#Specificity is also called the true negative rate.
# It Is the number of instances from the negative (second) class that were actually predicted correctly.


import warnings
warnings.filterwarnings(action="ignore")

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

filename = 'indians-diabetes.data.csv'
names=['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

kfold = KFold(n_splits=10 )
model = LogisticRegression()

scoringMethod = 'roc_auc'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print("AUC: %.3f (%.3f)" % ( results.mean()*100, results.std()*100 ) )



