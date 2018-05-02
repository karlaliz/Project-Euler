#Largest Palindrome product

def largestPalindrome():
	maxProduct=0
	for i in xrange (100,999+1):
		for e in xrange(i, 999+1):
			pNumber=i*e
			if str(pNumber)==str(pNumber)[::-1] and pNumber >maxProduct:
				maxProduct = pNumber
	return maxProduct

print (largestPalindrome())


