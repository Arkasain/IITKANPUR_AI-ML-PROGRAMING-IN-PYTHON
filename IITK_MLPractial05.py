# Load CSV Files with Pandas
# ============================================

import pandas
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_column', None)
pandas.set_option('display.width', 1000)

filename = "indians-diabetes.data.csv"
hnames = ['preg', 'plas', 'pres',
          'skin', 'test', 'mass',
          'pedi', 'age', 'class']
#
df = pandas.read_csv(filename, names=hnames)
print("Size of training data = ", df.shape)
#
print("\n\n")
print(df)
# print(df.dtypes)
# print("\n\n")
print("\n\n\n")
print(df.describe())