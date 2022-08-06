class Solution:
    
    def dfs(self, prev, cur, dep, adjList, depList):
        depList[cur] = dep
        
        for nei in adjList[cur]:
            if nei == prev:
                continue
            
            if depList[nei] == -1:
                self.dfs(cur, nei, dep + 1, adjList, depList)
            
            if depList[nei] > dep:
                self.ccList.append([cur, nei])
            
            depList[cur] = min(depList[cur], depList[nei])
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        adjList = [[] for i in range(n)]
        for  a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
        
        self.ccList = []
        depList = [-1] * n
        
        self.dfs(-1, 0, 0, adjList, depList)
        
        return self.ccList