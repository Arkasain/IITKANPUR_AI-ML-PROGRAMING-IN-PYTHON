import csv
filename = open('indians-diabetes.data.csv')
reader =csv.reader(filename, delimiter=',')
x = list(reader)
print('No of Rows:',len(x),'\n\n')
print('No of Col:',len(x[0]),'\n\n')
print("list of data \n ",x)

print("\n\n")
for row in x:
    print(row)