class Solution:
    def isPrime (self, N):
        # Time -> O(sqrt(N))
        # space -> O(1)
        if N <= 1:
            return 0
        
        i = 2
        while i * i <= N:
            if N % i == 0:
                return 0
            i += 1
                
        return 1