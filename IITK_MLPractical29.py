### "g-" --> green solid line
### "ro"  --> red circle dot
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'go-')
plt.xlabel("some numbers")
plt.ylabel("squared value")
plt.axis([-3,5,0,17])
plt.show()