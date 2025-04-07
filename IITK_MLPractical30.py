import matplotlib.pyplot as plt         #visualisaze the transforming values by matplotlib....
plt.plot([1,2,3,4,5],[1,2,3,4,5],'bo-', label='line1',linewidth=2)
plt.plot([1,2,3,4,5],[1,4,9,16,25],'rs-', label='line2',linewidth=10)

plt.axis ([0,6,0,26])

plt.legend(loc="upper left")

plt.show()
# ,11,12,13,14,16,17,18,19,20,,21,,23,,25,26,27,28,29,30