#matrix multiplication
q=input ("enter no of rows for matrix a:")
p=input ("enter no of columns for matrix a:")
n=input ("enter no of rows for matrix b:")
m=input ("enter no of columns for matrix b:")
a=[]
b=[]
c=[]
s=0
for i in range(q):
	x=[]
	for j in range(p):
		e=input ("enter element:")
		x.append(e)
	a.append(x)
print a
for i in range(n):
	y=[]
	for j in range(m):
		d=input ("enter element:")
		y.append(d)
	b.append(y)
print b
if (p==n):
	for i in range(q):
		f=[]
		for j in range(m):
			s=0
			for k in range(p):
				s=s+a[i][k]*b[k][j]
			f.append(s)
		c.append(f)
	print c
else:
	print "matrix multiplication is not possible"


