class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution - Dynamic Programming Tabulation
        # Time - O(N*M)
        # Space - O(M)
        
        h, w = len(dungeon), len(dungeon[0])
        
        pdp  = [0]*w
        
        for i in reversed(range(h)):
            cdp = [0]*w
            for j in reversed(range(w)):
                
                if i == h-1 and j == w-1:
                    cdp[j] = min(dungeon[i][j], 0)
                    continue
                    
                cost = float('-inf') + 1000
                if i + 1 < h:
                    cost = pdp[j]
                if j + 1 < w:
                    cost = max(cost, cdp[j+1])
                
                cdp[j] = min(0, cost + dungeon[i][j])
            
            pdp = cdp
        return abs(pdp[0]) +1

class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution - Dynamic Programming Tabulation
        # Time - O(N*M)
        # Space - O(N*M)
        
        h, w = len(dungeon), len(dungeon[0])
        
        dp  = [[0]*w for _ in range(h)]
        
        for i in reversed(range(h)):
            for j in reversed(range(w)):
                
                if i == h-1 and j == w-1:
                    dp[i][j] = min(dungeon[i][j], 0)
                    continue
                    
                cost = float('-inf') + 1000
                if i + 1 < h:
                    cost = dp[i+1][j]
                if j + 1 < w:
                    cost = max(cost, dp[i][j+1])
                
                dp[i][j] = min(0, cost + dungeon[i][j])
                
        return abs(dp[0][0]) +1

class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution - Recusion + Memoization
        # Time - O(N*M)
        # Space - O(N*M)
        
        self.memo = {}
        cost = self.recur(0, 0, dungeon)
        return abs(cost) + 1
    
    def recur(self, i, j, dungeon):
        h, w = len(dungeon), len(dungeon[0])
        
        if i >= h or j >= w:
            return float('-inf') + 1000
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i == h-1 and j == w-1:
            return min(dungeon[i][j], 0) 
        
        cost = max(self.recur(i + 1, j, dungeon),
                  self.recur(i, j + 1, dungeon)) + dungeon[i][j]
        
        self.memo[(i, j)] = min(cost, 0)
        
        return self.memo[(i, j)]