p = [2,3,5,7]
i= 105000

while len(p) < 7:
	for a in xrange(8,i):
		if a > 1:
			for x in xrange(2,a):
				if a%x==0:
					break
			else:
				p.append(a)

print p[10000]
print len(p)
