import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
#write data
f=open('sine.txt','w')
f.write(str(x))
f.close()
#read data
f=open('sine.txt','r')
y=f.read()
print(y)
f.close