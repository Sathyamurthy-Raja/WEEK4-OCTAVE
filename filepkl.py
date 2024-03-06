import numpy as np
import pickle as pkl
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
#write data
output_file=open('sine_pkl.txt','wb')
pkl.dump(x,output_file)
output_file.close()
#read data
input_file=open('sine_pkl.txt','rb')
y=pkl.load(input_file)
print(y)
input_file.close()