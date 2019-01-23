import numpy as np
import matplotlib.pyplot as plot
def x(a,w,p):
	s=a*np.cos((w*t)+p)
	return s
t=np.arange(0,100,1)
a1=input("enter an amplitude a1:")
a2=input("enter another amplitude a2:")
w1=input("enter a frequency w1:")
w2=input("enter a frequency w2:")
p1=input("enter a phase p1:")
p2=input("enter another phase p2:")
x1=x(a1,w1,p1)
x2=x(a2,w1,p1)
x3=x(a1,w2,p1)
x4=x(a1,w1,p2)
q=x1+x2
r=x1+x3
s=x1+x4
plot.subplot(3,1,1)
plot.plot(t,q,'r')
plot.subplot(3,1,2)
plot.plot(t,r,'b')
plot.subplot(3,1,3)
plot.plot(t,s,'g')
plot.show()
