import warnings
warnings.filterwarnings(action='ignore')
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix

hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv("indians-diabetes.data.csv",names=hnames)
scatter_matrix(dataframe)
plt.show()