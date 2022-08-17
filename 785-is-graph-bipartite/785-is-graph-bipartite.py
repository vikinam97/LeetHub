class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
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
        bfsList = [(cur, 'A')]
        while bfsList:
            nxt = []
            for i, color in bfsList:
                if i in nodeColors:
                    if nodeColors[i] != color:
                        return False
                else:
                    nodeColors[i] = color
                    for child in graph[i]:
                        nxt.append((child, 'B' if color == 'A' else 'A'))
            bfsList = nxt
        return True
        