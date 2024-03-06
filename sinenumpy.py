import numpy as np
import csv
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
#write data
with open('sine.csv','w') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([x])
    newFile.close()
#read data
with open('sine.csv','r') as newFile:
    newFileReader = csv.reader(newFile)
    for row in newFileReader:
        print (row)
    newFile.close()