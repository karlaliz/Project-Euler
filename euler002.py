#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
def fibonacci(n):
	a=0
	b=1
	while n > 1:
		n=n-1
		a,b = b, a+b
	return b

def sumEvenValued():
	add=0
	for e in range(1,60+2):
		v=fibonacci(e)
		if v <= 4*1000*1000:
			if v % 2 ==0: #calculate if it is even number 
				add+=v
	return add

print sumEvenValued()