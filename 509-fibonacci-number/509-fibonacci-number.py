class Solution:
    def fib(self, n: int) -> int:
        ratio = (sqrt(5) + 1) / 2;
        
        uptopowers = 1;
        while n > 0: 
            if(n & 1):
                uptopowers *= ratio;
            ratio = ratio * ratio;
            n = n >> 1; 
        
        return round(uptopowers / sqrt(5));
    
    def fib1(self, n: int) -> int:
        # Solution - Simple trversal
        # Time - O(N)
        # Space - O(1)
        if n == 0:
            return 0
        a = 0
        b = 1
        for i in range(1, n):
            a, b = b, a+b
        
        return b
    