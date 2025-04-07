#Q1)
import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,10,20,30,40,50])
y=(x*3)
plt.plot(x,y, linestyle='-', color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('Draw a line')
plt.show()
#Q2)
import matplotlib.pyplot as plt
x = [2, 3, 4]
y = [2, 4, 1]
plt.plot(x, y, linestyle='-', color='b')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
#Q3)
import matplotlib.pyplot as plt
x = []
y = []
with open('dummy.txt', 'r') as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))
plt.plot(x, y, linestyle='-', color='b')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
#Q4)
import matplotlib.pyplot as plt
open_prices = [774.25, 776.030029, 779.309998, 779, 779.659973]
high_prices = [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
low_prices = [769.5, 772.890015, 775.650024, 775.539978, 770.75]
close_prices = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
plt.plot(open_prices, label='Open')
plt.plot( high_prices, label='High')
plt.plot( low_prices, label='Low')
plt.plot( close_prices, label='Close')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data')
plt.show()
#Q5)
import matplotlib.pyplot as plt
x1 = [10, 20,30]
x2=[10,20,30]
y1 = [20, 40,10]
y2 = [40, 10,30]
plt.plot(x1, y1, label='line 1', color='blue')
plt.plot(x2, y2, label='line 2', color='green')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.show()
#Q6)
import matplotlib.pyplot as plt
x1=[10, 20,30]
x2=[10,20,30]
y1=[20, 40,10]
y2=[40, 10,30]
plt.plot(x1, y1, label='line 1-width-3', color='blue',linewidth=3)
plt.plot(x2, y2, label='line 2-width-5', color='red',linewidth=5)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()
#Q7)
import matplotlib.pyplot as plt
x1=[10, 20,30]
x2=[10,20,30]
y1=[20, 40,10]
y2=[40, 10,30]
plt.plot(x1, y1, label='line 1-dotted',linestyle=":", color='blue',linewidth=3)
plt.plot(x2, y2, label='line 2-dashed',linestyle="--",color='red',linewidth=5)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('plot two or more lines with different style')
plt.legend()
plt.show()
#Q8)
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,4,5,6,7])
y = np.array([2,6,3,6,3])
plt.plot(x,y, linestyle=':', color='red', marker='o',
         markerfacecolor='blue', markersize=10)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')
plt.axis([1,8,1,8,])
plt.legend(["Data Points"])
plt.show()
#Q9)
import matplotlib.pyplot as plt
import numpy as np
x =np.array([0,10,20,30,40,50])
y =x*3
plt.plot(x, y, label='y = 3x', color='blue')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
current_limits = plt.axis([0,100,0,200])
print(f"Current axis limits: {current_limits}")
plt.xlim(0, 100)
plt.ylim(0, 200)
plt.legend()
plt.show()
#Q10)
import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
x2 = np.array([2, 4, 6, 8, 10])
y2 = np.array([5, 10, 15, 20, 25])
plt.scatter(x1,y1,color='blue',marker='o',label='Set 1',s=4)
plt.scatter(x2,y2,color='red',marker='o',label='Set 2',s=7)
plt.xlim(0, 10)
plt.ylim(0, 30)
plt.show()
#Q11)
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 5, 0.2)
y1 = x**2
y2 = x**3
y3 = x*1
plt.plot(x, y1, 'bs')
plt.plot(x, y2, 'r^')
plt.plot(x, y3, 'g--')
plt.xlim(0, 5)
plt.ylim(0, 120)
plt.show()
#Q12)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
dates = [ datetime.date(2016, 10, 3),
    datetime.date(2016, 10, 4),
    datetime.date(2016, 10, 5),
    datetime.date(2016, 10, 6),
    datetime.date(2016, 10, 7),]
values = [772.5, 776.5,776.5,776.8,775.2]
plt.plot(dates, values, 'ro-')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()
plt.show()
#Q13)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
dates = [
    datetime.date(2016, 10, 3),
    datetime.date(2016, 10, 4),
    datetime.date(2016, 10, 5),
    datetime.date(2016, 10, 6),
    datetime.date(2016, 10, 7),
]
values = [772.5, 776.5,776.5,776.8,775.2]
plt.plot(dates, values, 'ro-', label="Value over Time")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Date format
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('closing value')
plt.title('closing stock value of alphabet inc')
plt.grid(True)
plt.show()
#Q14)
import matplotlib.pyplot as plt
import numpy as np
x=['2016-10-03','2016-10-04','2016-10-05','2016-10-06','2016-10-07']
y=np.array([772.559998,776.429993,776.469971,776.859985,775.080017])
plt.plot(x,y,'ro-')
plt.axis(['2016-10-03','2016-10-07',772.5,777.0])
plt.xlabel("Date")
plt.ylabel("Closing Value")
plt.title("Closing stock value of Alphabet Inc")
plt.grid(which='major',color='red',linewidth=0.5,linestyle='-')
plt.grid(which='minor',color='blue',linewidth=0.2,linestyle=':')
plt.tick_params(left=False, bottom=False)
plt.show()