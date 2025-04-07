from matplotlib import pyplot as plt
import pandas
filename = 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pandas.read_csv(filename,names=hnames)
df.plot(kind='box',subplots=True,layout=(3,3),sharex=False,sharey=False)
plt.tight_layout()
plt.show()