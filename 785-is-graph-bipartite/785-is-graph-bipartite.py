class Solution:
    
    def bfs(self, cur, nodeColors, path, graph):
        
        if cur in nodeColors:
            return True
        
        bfs = [(cur, 'A')]
        
        while bfs:
            nxt = []
            for i, color in bfs:
                if i in nodeColors:
                    if nodeColors[i] != color:
                        return False
                else:
                    nodeColors[i] = color
                    for child in graph[i]:
                        nxt.append((child, 'B' if color == 'A' else 'A'))
            bfs = nxt
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColors = {}
        for i in range(len(graph)):
            if not self.bfs(i, nodeColors, set(), graph):
                return False
        return True
        