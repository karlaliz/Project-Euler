#10001st prime
import math

def isPrimeNumber(n):
	sqr = int(math.sqrt(n)) + 1;
	for e in range(2, sqr):
		if n%e ==0:
			return False
	return True

def listPrime():
	count=0
	number=0
	for i in range(2,2000000):
		if isPrimeNumber(i)== True:
			count+=1
			number=i
		if count ==10001:
			return i
			break

print(listPrime())