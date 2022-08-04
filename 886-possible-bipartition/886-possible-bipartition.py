class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjMat = [0] * n
        
        for v in range(len(adjMat)):
            adjMat[v] = []
        
        for i in range(len(dislikes)):
            a, b = dislikes[i]
            adjMat[a-1].append(b-1)
            adjMat[b-1].append(a-1)
        
        return self.isBipartite(adjMat)
        
    def isBipartite(self, graph):
        # Solution - BFS - graph coloring
        # Time - O(V+E)
        # Space - O(V)
        
        nodeColors = {}
        for i in range(len(graph)):
            if not self.bfs(i, nodeColors, set(), graph):
                return False
        return True
    
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