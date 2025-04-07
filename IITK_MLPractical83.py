import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
data = pd.read_csv('LinearRegressionPoly_Data.csv')
print(data)
print(data.shape)  # (7, 2)

X = data.iloc[:, 0:1].values  # [ rows, cols ]
y = data.iloc[:, 1].values  # [ rows, cols ]
print("X.shape = ", X.shape, "\n X=\n", X)
print("y.shape = ", y.shape, "\n y=", y)

# Step: Fitting Linear Regression to the dataset
# Fitting the linear Regression model on two components X and y.
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(X, y)
# estimate the parameters of the model
y_dash = lin.predict(X)

plt.scatter(X, y, color='blue')
plt.scatter(X, y_dash, color='m')
plt.plot(X, y_dash, color='red')
plt.title('Linear Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X)
print('X=\n', X)
print('X_poly=\n', X_poly)

lin2 =LinearRegression()
lin2.fit(X_poly, y)

plt.scatter(X, y, color='Blue')
y_pred=lin2.predict(X_poly)
plt.plot(X, y_pred, color='red')
plt.title('Polynomial Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')
plt.show()