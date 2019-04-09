import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
w=2000
Sp=0.8
Ss=0.2
Wp=2000*np.pi
Ws=5000*np.pi
x=0.5*np.log(((1/(Sp)**2)-1)/((1/(Ss)**2)-1))/np.log(Wp/Ws)
N=np.ceil(x)
Wc=Wp/(((1/(Sp)**2)-1))**(1/2*N)
H=[]
for i in range(w):
	a=float(1/np.sqrt((1+(2*np.pi*i/Wc)**(2*N))))
	H.append(a)
print N,Wc
plot.plot(H,'g')
plot.show()

