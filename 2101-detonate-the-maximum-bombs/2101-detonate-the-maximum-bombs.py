class Solution:        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Solution - BFS - for every bomb
        # Time - O(N^2)
        # Space - O(N)
        maxSoFar, maxi = 0, -1
        for i in range(len(bombs)):
            tmax = self.bfs(i, bombs)
            if maxSoFar < tmax:
                maxSoFar, maxi = tmax, i
        
        return maxSoFar
        
    def bfs(self, cur, bombs):
        bfsList = [(bombs[cur], cur)]
        detonatedMap = { cur: True }
        
        count = 0
        while bfsList:
            nxt = []
            for bomb, idx in bfsList:
                x, y, r = bomb
                count += 1
                for id2 in range(len(bombs)):
                    xi, yi, ri = bombs[id2]
                    if id2 not in detonatedMap and math.dist([x, y], [xi, yi]) <= r:
                        nxt.append((bombs[id2], id2))
                        detonatedMap[id2] = True
            bfsList = nxt
        return count
            