

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        #dp[i][j] = Number of floors that can be checked with i drops & j eggs
        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,1+k):
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
            if dp[i][k]>=n:
                return i


class Solution1:
    def recur(self, eggs, floors):
        if eggs == 1 or floors <= 1:
            return floors
        
        if (eggs, floors) in self.memo:
            return self.memo[(eggs, floors)]
            
        minMoves = float('inf')
        for i in range(1, floors+1):
            brk, ntBrk = self.recur(eggs-1, i-1), self.recur(eggs, floors - i)
            
            moves = 1 + max(brk, ntBrk)
            
            minMoves = min(minMoves, moves)
        
        self.memo[(eggs, floors)] = minMoves
        return minMoves
    
    def superEggDrop(self, k: int, n: int) -> int:
        self.memo = {}
        return self.recur(k, n)