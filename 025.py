i=0
F = [1,1]
while F[i] < 10**999 :
	F.insert(0,F[1]+F[0])
print len(F)
print F[0]


