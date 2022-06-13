class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        def SieveOfEratosthenes(n):
            prime = [True for i in range(n + 1)]
            prime[0], prime[1] = False, False  # 0 and 1 aren't primes

            p = 2
            while p * p <= n:
                if prime[p] == True:
                    for i in range(p * 2, n + 1, p):
                        prime[i] = False
                p += 1

            numberOfPrimes = 0
            for p in range(n):
                if prime[p]:
                    numberOfPrimes += 1
            return numberOfPrimes

        return SieveOfEratosthenes(n)
        
#         if n <= 1:
#             return 0
        
#         striverList = [True] * n
        
#         striverList[0] = striverList[1] = False
        
#         for i in range(2, math.isqrt(n) + 1):
#             if striverList[i] == False:
#                 continue
#             j = i * i
#             while j < n:
#                 striverList[j] = False
#                 j += i
            
#         count = 0
#         for i in range(2, n):
#             if striverList[i] == True:
#                 count += 1
        
#         return count
            
                
        