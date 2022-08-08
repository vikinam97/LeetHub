class DSUF:
    def __init__(self, n):
        self.arr = [-1] * n
    
    def find(self, node):
        if self.arr[node] == -1:
            return node
        self.arr[node] = self.find(self.arr[node])
        return self.arr[node]
    
    def union(self, a, b):
        aP = self.find(a)
        bP = self.find(b)
        if aP == bP:
            return 
        self.arr[aP] = bP
        
    def countParent(self):
        count = 0
        for i in self.arr:
            if i == -1:
                count += 1
        return count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        dSet = DSUF(V)
        
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1:
                    dSet.union(i, j)
        
        return dSet.countParent()
    
class Solution1:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Solution - DFS
        # Time - O(V+E)
        # Space - O(V+E)
        
        count = 0
        height, width = len(isConnected), len(isConnected[0])
        
        adjList = defaultdict(list)
        for i in range(height):
            for j in range(width):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
        
        self.visited = [0] * height
        
        for i in range(height):
            if self.visited[i] != 0:
                continue
            self.dfs(i, adjList)
            count += 1
                    
        return count
    
    def dfs(self, cur, adjList):
        if self.visited[cur] != 0:
            return
        
        self.visited[cur] = 1
        
        for node in adjList[cur]:
            self.dfs(node, adjList)