factors = []

def isPrimeFactor(n):
	i=2
	while i <= n:
		if n%i ==0:
			n = n/i
			factors.append(i)
		else:
			i = i + 1
isPrimeFactor(600851475143)
print factors
print (int(max(factors)))