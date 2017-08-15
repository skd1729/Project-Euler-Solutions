with open("largeproduct.txt") as k:
	m=k.read().splitlines()
m = [x.strip() for x in m]
#print join(m)
B = ''.join(map(str, m))
M = [1]
T = [0]
print len(B)
for i in range(0,988):
	for k in range(i,i+13):
		M[0] = int(B[k]) * M[0]
		
	if T[0] < M[0]:
		T[0]=M[0]
	M = [1]
print T[0]

	












