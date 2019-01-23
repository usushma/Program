import numpy as np
import matplotlib.pyplot as plot
f1=20
f2=10
f=500
n=np.arange(0,1000,1)
a1=np.cos(2*(3.14)*(f1/f)*n)
a2=np.cos(2*(3.14)*(f2/f)*n)
a=a1+a2
plot.subplot(3,1,1)
plot.plot(n,a1,'r')
plot.subplot(3,1,2)
plot.plot(n,a2,'b')
plot.subplot(3,1,3)
plot.plot(n,a,'g')
plot.show()
