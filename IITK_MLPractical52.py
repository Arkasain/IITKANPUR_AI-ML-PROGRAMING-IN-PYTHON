import pandas as pd
data =pd.read_csv("employees_with_missing_data - employees_with_missing_data.csv")
print("\n\noriginal data=\n",data)
data2=data.dropna(axis=0,how='any') ### making new data frame with dropped na valaues  ### 'any' is default for how , 0 for rows
print("\n\n filtered data=\n",data2)
print("\n old data frame len:",len(data))
print("\n new data frame len:",len(data2))
print("\n number of the rows with at least 1 na value:",(len(data)-len(data2)))
