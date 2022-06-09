class Solution:
    def isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = 0
        for i in range(left, right + 1):
            num = bin(i).count('1')
            if self.isPrime(num):
                primes += 1
        return primes
        