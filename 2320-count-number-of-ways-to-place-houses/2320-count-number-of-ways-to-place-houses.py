class Solution:
    def countHousePlacements(self, n: int) -> int:
#         def fib(x):
#             a, b, c = 1, 1, 0
            
#             for _ in range(x):
#                 c = a + b
#                 b, a = c, b
            
#             return c
        a, b = 1, 1
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            ans = a + b
            a = b
            b = ans
    
        return ((ans% MOD) * (ans% MOD)) % MOD
# class Solution:
#     def countHousePlacements(self, n: int) -> int:
#         def fib(x):
#             a, b, c = 1, 1, 0
            
#             for _ in range(x):
#                 c = a + b
#                 b, a = c, b
            
#             return c
            
#         return (fib(n)) ** 2 % (10 ** 9 + 7)