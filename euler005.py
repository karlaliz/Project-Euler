#smallest multiple

def isMultiple(n):
	for i in range(2,20+1):
		if n%i != 0:
			return False
	else:
		return True

def smallestMultiple():
	for e in xrange(1, 1*100*100*100*100*100):
		if isMultiple(e)== True:
			return e
			break 

print(smallestMultiple())			