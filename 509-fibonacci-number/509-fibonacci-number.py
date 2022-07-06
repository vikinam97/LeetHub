class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        b = 1
        for i in range(1, n):
            a, b = b, a+b
        
        return b