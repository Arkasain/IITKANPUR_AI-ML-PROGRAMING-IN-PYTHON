import numpy
import urllib.request
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path, delimiter=",")
print("shape of data from url (Rows and cols) : " , dataset.shape )
print("format of data dim = ", dataset.ndim)
# print('No of Col:',len(dataset[0]),'\n\n')
# print('No of rows:',len(dataset),'\n\n')
print(dataset)