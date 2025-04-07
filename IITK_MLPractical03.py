import numpy
filename=open("indians-diabetes.data.csv")
data = numpy.loadtxt(filename,delimiter=',')
filename.close()
print("numpy loadtxt size = ",data.shape )
print("data : \n" , data)