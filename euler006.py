#Sum square difference
def squares(n):
	return n*n

def squareDifference():
	sq=0
	su=0
	for e in range(1, 100+1):
		su=su+e
		sq=sq+ squares(e)
	return su*su-sq

print(squareDifference())