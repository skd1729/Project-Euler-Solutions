a=0
sum=0
F = [2,1]
while F[0]<4000000 :
	c=F[0]+F[1] 
	F.insert(0,c)

print F
for a in range(len(F)):
	if F[a]<=4000000 and F[a]%2==0:
		sum = sum + F[a]
	a=a+1
print sum
