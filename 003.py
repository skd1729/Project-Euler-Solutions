 #600851475143
 #This code is a kind of brute force. The trick lies in the factorization of large number
 # I ran the code with 20000 in xrange as upper limit to find the factors first to decrease the number
p=[]
x=1
i= 600851475143
while x in xrange(1,7000):
	if i%x==0 and x>1:
		p.append(x)
		i=i/x
		x=0
	x=x+1
print p
# The above code gives the output p=[71,839,1471,6857]
# to double check, verify that 71*839*1471*6857 = 600851475143. We break these factors into different primes now
a=0
for a < len(p):
	for k in xrange(2,int(p[a]/2)):
		if p[a]%k ==0:
		break
