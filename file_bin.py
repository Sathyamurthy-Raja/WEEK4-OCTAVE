import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
#write data
f=open('sine_bin.txt','wb')
f.write((x))
f.close()
#read data
f=open('sine_bin.txt','rb')
y=f.read()
print(y)
f.close