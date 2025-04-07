import matplotlib.pyplot as plt
import pandas as pd
import numpy
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv('indians-diabetes.data.csv',names=hnames)
correlations=dataframe.corr()  #### plot correlation matirx
print(correlations) #### following will add matrix and side bar in entire area
fig = plt.figure()
subFig = fig.add_subplot(111)
cax=subFig.matshow(correlations, vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=numpy.arange(0,9)
subFig.set_xticks(ticks)
subFig.set_yticks(ticks)
subFig.set_xticklabels(hnames)
subFig.set_yticklabels(hnames)

plt.show()
