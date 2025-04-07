import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_column',None)
pd.set_option('display.width',1000)

data = pd.read_csv("employees_with_missing_data - employees_with_missing_data.csv")


bool_series=data["Gender"].isnull()
# bool_series=data["First Name"].isnull()

print(bool_series)


result=data[bool_series]
print(result)
# print(result.shape)
# print(result.info())