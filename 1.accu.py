import numpy as np
import matplotlib.pyplot as plot
m=input("enter length of the pulse train:")
p=0
q=0
s=[]
z=[]
for i in range(m):
	q=q+np.sin(i*2.0*np.pi*10/500)
	s.append(q)
for i in range(m):
	p=p+1
	z.append(p)
n=np.arange(0, m, 1)
plot.subplot(211)
plot.stem(n,s,'g')
plot.subplot(212)
plot.stem(n,z,'b')
plot.show()

