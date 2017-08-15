p=[]
for x in range(100,1000):
	for i in range(x*100,x*1000,x):
		a=[int(i) for i in str(i)]
		if  (a==a[::-1]):
			#print a
			num = int(''.join(map(str,a)))
			
			p.append(num)
		
p.sort()
print p[-1]
