# Practical Implementation of Linear Regression using sklearn
import warnings

warnings.filterwarnings(action="ignore")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_training_data(filename):
    dataframe = pd.read_csv(filename)
    print(dataframe)
    x_parameter = []
    y_parameter = []

    for single_square_feet, single_price in zip(dataframe['square_feet'], dataframe['price']):
        x_parameter.append([single_square_feet])
        y_parameter.append(single_price)

        # Once we got the data , return it to main program
        return x_parameter, y_parameter


def train_linear_model(x_parameter, y_parameter, quest_value):
    # create linear regression object
    regr = LinearRegression()
    regr.fit(x_parameter, y_parameter)  # m & c  # Algo has been trained by fit()
    predicted_ans = regr.predict([[700]])
    print("Output from machine = ", predicted_ans)

    print("After Training via sklearn : Model Parameters")
    print("m = ", regr.coef_)  # m
    print("c = ", regr.intercept_)  # c
    print("sklearn generated Model : y = ", regr.coef_, " * x + ", regr.intercept_)
    plt.scatter(x_parameter, y_parameter, color="m", marker="o")
    all_predicted_y = regr.predict(x_parameter)
    plt.scatter(x_parameter, all_predicted_y, color="b", marker="o")
    plt.plot(x_parameter, all_predicted_y, color="g")
    plt.scatter(quest_value, predicted_ans, color="r")
    plt.show()


def startAIAlgorithm():
    # Collect the training data from external CSV data file.
    x, y = get_training_data("LR_House_price.csv")
    print("Formatted Training data : ")
    print("x = ", x)


if __name__ == "_main_":
    startAIAlgorithm()