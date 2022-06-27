# class Solution:
#     def countHousePlacements(self, n: int) -> int:
#         a, b = 0, 1
#         ans = 1
#         MOD = math.pow(10, 9) + 7
#         for i in range(n):
#             temp = a + b
#             a = b
#             b = temp
#             ans = (a + b) % MOD
        
#         return int((ans%MOD) * (ans%MOD))
    
class Solution:
    def countHousePlacements(self, n: int) -> int:
        def fib(x):
            a, b, c = 1, 1, 0
            
            for _ in range(x):
                c = a + b
                b, a = c, b
            
            return c
            
        return (fib(n)) ** 2 % (10 ** 9 + 7)