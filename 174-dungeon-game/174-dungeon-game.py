class Solution:
    
    def recur(self, i, j, dungeon):
        h, w = len(dungeon), len(dungeon[0])
        if i >= h or j >= w:
            return float('-inf') + 1000
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i == h-1 and j == w-1:
            return dungeon[i][j] if dungeon[i][j] < 0 else 0 
        
        cost = max(self.recur(i + 1, j, dungeon),
                  self.recur(i, j + 1, dungeon)) + dungeon[i][j]
        
        self.memo[(i, j)] = cost if cost < 0 else 0
        
        return self.memo[(i, j)]
    
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.memo = {}
        cost = self.recur(0, 0, dungeon)
        # print(self.memo)
        return abs(cost) + 1