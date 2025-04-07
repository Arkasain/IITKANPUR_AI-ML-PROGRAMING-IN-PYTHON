import matplotlib.pyplot as plt


mylabels =['s1','s2','s3']
section =[60,90,50]
mycolors=['c','g','r']
plt.pie(section , labels=mylabels, colors=mycolors, startangle=90, explode=(0,0,0.2), autopct='%.f%%')
plt.title('pie chart example')
plt.show()