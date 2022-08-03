class Solution:
    
    def dfs(self, cur, dest, graph, path):
        if cur == dest:
            self.paths.append(path[:] + [dest])
        
        if cur in path:
            return
        
        path.append(cur)
        for i in graph[cur]:
            self.dfs(i, dest, graph, path)
        path.pop()
        
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.dfs(0, len(graph)-1, graph, [])
        return self.paths