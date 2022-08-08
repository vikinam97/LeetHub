class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adjMat = defaultdict(set)
        degree = [0] * (n+1)
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            adjMat[min(u, v)].add(max(u, v))
            
        minSoFar = float('inf')
        
        for n1 in range(1, n+1):
            for n2 in adjMat[n1]:
                for n3 in adjMat[n1]:
                    if n3 in adjMat[n2]:
                        minSoFar = min(minSoFar, degree[n1] + degree[n2] + degree[n3] - 6)
        
        return minSoFar if minSoFar != float('inf') else -1