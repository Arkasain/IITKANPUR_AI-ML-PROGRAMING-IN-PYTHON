import pandas as pd
data=pd.read_csv("employees_with_missing_data - employees_with_missing_data.csv")


print("Original Data=\n", data[10:25] )

df2=data["Gender"].fillna("No Gender")

print("\n\n\n Data after filling=\n", df2[10:25] )