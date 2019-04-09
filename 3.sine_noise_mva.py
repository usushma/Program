import numpy as np
import matplotlib.pyplot as plot
def t(j):
	x=np.sin(n*2*np.pi*10/50)
	z=np.random.rand(x.shape[0])
	c=x+z
	return c
def y(p):
	s=0
	for i in range(p):
		u=t(n-i)
		y=(1.0/p)*u
		s=s+y
	return s
p=input("enter the order of the system:")
n=np.arange(0, 10, 0.1)
wave=np.sin(n*2*np.pi*10/50)
noise=np.random.rand(wave.shape[0])
mix=wave+noise
plot.subplot(411)
plot.plot(n,wave,'g')
plot.subplot(412)
plot.plot(n,noise,'r')
plot.subplot(413)
plot.plot(n,mix,'b')
plot.subplot(414)
plot.plot(n,y(p),'k')
plot.show()

