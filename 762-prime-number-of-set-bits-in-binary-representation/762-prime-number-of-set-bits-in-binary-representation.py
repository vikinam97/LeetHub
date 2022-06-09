class Solution:
    # def isPrime(self, num):
    #     if num <= 1:
    #         return False
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False
    #     return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
#         primes = 0
        
#         for i in range(left, right + 1):
#             num = bin(i).count('1')
#             if self.isPrime(num):
#                 primes += 1
#         return primes

        
        resCount  = 0
        primeSet = {1: False}
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
#             if primeSet.get(n) != None:
#                 return primeSet.get(n)
#             for i in range(2, n//2):
#                 if n % i == 0:
#                     primeSet[n] = False
#                     return False
                
#             primeSet[n] = True
#             return True
        
        def countSetBit(n):
            count = 0
            while n != 0:
                count += 1
                n = n & (n-1)
            return count
        
        for num in range(left, right+1):
            noSetBit = countSetBit(num)
            print(num, " => ", noSetBit, isPrime(noSetBit))
            if isPrime(noSetBit) == True:
                resCount += 1
                
        return resCount
        