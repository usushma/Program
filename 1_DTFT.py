import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
j=cm.sqrt(-1)
#x=input("enter a list of values:")
x=[4,5,8,1,3,9,10,25,33,0,3] 
w=np.linspace(-np.pi,np.pi,1000)
X=[]
for i in range(0,1000):
       w_tmp=w[i]
       s=0
       for k in range(0,len(x)):
            s+=(x[k]*np.exp(-k*w_tmp*j))
       X.append(s)
m=np.abs(X)
p=np.angle(X)
plot.subplot(3,1,1)
plot.plot(w,X,'r')
plot.subplot(3,1,2)
plot.plot(w,m,'b')
plot.subplot(3,1,3)
plot.plot(w,p,'g')
plot.show()
