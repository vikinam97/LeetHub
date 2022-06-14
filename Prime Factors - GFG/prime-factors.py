#User function Template for python3

class Solution:
	def AllPrimeFactors(self, N):
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

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends