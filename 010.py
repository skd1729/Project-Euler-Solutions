P = []
L= []
for x in range(2,2000001):
	P.append(x)

for i in range (2,1415):
	P = [x for x in P if x%i != 0 or x ==i]
	#print "The length of P is" , len(P)
sum = 0
for i in range(0,len(P)):
	sum = sum + P[i]
print sum





