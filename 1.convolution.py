import numpy as np
import matplotlib.pyplot as plt
m=input("enter length of x:")
z=input("enter length of h:")
x=[]
h=[]
y=[]
p=m+z-1
n=np.arange(0, p, 1)
for i in range(m):
	c=input("enter an element:")
	x.append(c)
for i in range(z):
	d=input("enter an element:")
	h.append(d)
while(m<p):
	x.append(0)
	m=m+1
for i in range(p):
	s=0
	for j in range(z):
		q=h[j]*x[i-j]
		s=s+q
	y.append(s)
plt.stem(n,y)
plt.show()
