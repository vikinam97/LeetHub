```
class Solution:
	def AllPrimeFactors(self, N):
        # Time O(sqrt(n))
        # Space O(1)
		primesList = []
		i = 2
		while i * i <= N:
		    if N % i == 0:
		        primesList.append(i)
		    while N % i == 0:
		        N = N // i
		    i += 1
	    
	    if N > 1:
	        primesList.append(N)
	    
	    return primesList
```