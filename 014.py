le = [0]
for x in range(2,1000001):
	t= x
	c = 0
	while t!=1:
		if t%2 == 0:
			t=t/2
		else:
			t = 3*t+1
		c = c+1
	if le[0] < c:
		f=[x]
		le[0] = c
print f
 

