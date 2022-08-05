class Solution:
    
    
    def dfs(self, cur, adjList):
        if self.visited[cur] != 0:
            return
        
        self.visited[cur] = 1
        
        for node in adjList[cur]:
            self.dfs(node, adjList)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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