i=1
fac=1
x=0
sum =0
for i in range(1,101):
	fac=fac*i
print fac
print len(str(fac))
d=[int(a) for a in str(fac)]
print d
for x in range(0, len(d)):
	sum = sum + d[x]
	x=x+1
print sum

	





