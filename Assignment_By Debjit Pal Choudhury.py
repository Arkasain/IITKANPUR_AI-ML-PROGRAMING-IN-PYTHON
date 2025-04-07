#1
import matplotlib.pyplot as plt
plt.plot([1,48],[1*3,48*3],'b') #Note: Value of y is 3 times of x
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Draw a line")
plt.axis([0,50,0,160])
plt.show()
#2
import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,4,1],'b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis([1,3,1,4])
plt.title('GRAPH')
plt.show()
#2
import matplotlib.pyplot as plt

# Read data from a file
def read_data(file_path):
    x_values, y_values = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            x_values.append(x)
            y_values.append(y)
    return x_values, y_values

x_values, y_values = read_data('Dummy.txt')
plt.plot(x_values, y_values, 'b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis([1, 3, 1, 4])
plt.title('Dummy Data')
plt.show()

#4
import matplotlib.pyplot as plt
from holoviews.plotting.bokeh.styles import marker

date=['03','04','05','06','07']
open_prices = [774.25, 776.030029, 779.309998, 779, 779.659973]
high_prices = [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
low_prices = [769.5, 772.890015, 775.650024, 775.539978, 770.75]
close_prices = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]

plt.plot(date,open_prices,label='Open',color='c')
plt.plot(date,high_prices,label='High',color='y')
plt.plot(date,low_prices,label='Low',color='g')
plt.plot(date,close_prices,label='Close',color='r')

plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

#5
import matplotlib.pyplot as plt
x=[10,20,30]
line_1=[20,40,10]
line_2=[40,10,30]
plt.plot(x,line_1,label='line 1',color='b')
plt.plot(x,line_2,label='line 2',color='g')
plt.title("Two or more lines on same plot with suitable legends")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis([10,30,10,40])
plt.legend()
plt.show()

#6
import matplotlib.pyplot as plt
x=[10,20,30]
line_1=[20,40,10]
line_2=[40,10,30]
plt.plot(x,line_1,label='line 1',color='r',linewidth=3)
plt.plot(x,line_2,label='line 2',color='b',linewidth=5)
plt.title("Two or more lines on same plot with suitable legends")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis([10,30,10,40])
plt.legend()
plt.show()

#7
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x=[10,20,30]
line_1=[20,40,10]
line_2=[40,10,30]
plt.plot(x,line_1,label='line 1-dotted',color='b',linestyle=':')
plt.plot(x,line_2,label='line 2-dashed',color='r',linestyle='--')
plt.title("Plot with two or more lines with different style")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis([10,30,10,40])
plt.legend()
plt.show()

#8
import matplotlib.pyplot as plt
plt.plot([1,4,5,6,7],[2,6,3,6,3],'ro:',markerfacecolor='b')
plt.axis([1,8,1,8])
plt.show()

#9
import matplotlib.pyplot as plt
x=[0,20,40,50]
y=[i*3 for i in x]
plt.plot(x,y)
plt.axis([0,100,0,200])
plt.title('Draw a line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#10
import matplotlib.pyplot as plt
plt.scatter([2,3,5,6,8],[1,5,11,19,21],color='b',s=5)
plt.scatter([3,4,6,7,9],[2,6,12,22,24],color='r',s=10)
plt.axis([0,10,0,30])
plt.show()

#11
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,5,0.2)
y1=x**2
y2=x**3
y3=x*1
plt.plot(x,y1,'s',x,y2,'r^',x,y3,'c:')
plt.xlim(0,5)
plt.ylim(0,120)
plt.show()

#12
import matplotlib.pyplot as plt
date=['2016-10-03','2016-10-04','2016-10-05','2026-10-06','2016-10-07']
y=[772.55998,776.429993,776.469971,776.859985,775.080017]
plt.plot(date,y,'ro-')
plt.axis(['2016-10-03','2016-10-07',772.5,777.0])
plt.show()

#13
import matplotlib.pyplot as plt
date=['2016-10-03','2016-10-04','2016-10-05','2026-10-06','2016-10-07']
y=[772.55998,776.429993,776.469971,776.859985,775.080017]
plt.plot(date,y,'ro-')
plt.grid(True,linestyle='-',color='b',linewidth=0.5)
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing stock value of Alphabet Inc.')
plt.axis(['2016-10-03','2016-10-07',772.5,777.0])
plt.show()

#14
import matplotlib.pyplot as plt
date=['2016-10-03','2016-10-04','2016-10-05','2026-10-06','2016-10-07']
y=[772.55998,776.429993,776.469971,776.859985,775.080017]
plt.plot(date,y,'ro-')
plt.grid(True,'major',linestyle='-',color='r',linewidth=0.8)
plt.minorticks_on()
plt.grid(True,'minor',linestyle=':',linewidth=0.4,color='r')
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing stock value of Alphabet Inc.')
plt.axis(['2016-10-03','2016-10-07',772.5,777.0])
plt.show()


