class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        adjMat = defaultdict(list)
        
        for i in range(len(edges)):
            a, b = edges[i]
            adjMat[a].append((b, succProb[i]))
            adjMat[b].append((a, succProb[i]))
            
        dist = [float('-inf')] * n
        visited = [-1] * n
        dist[start] = 1
        
        heap = [(1, start)]
        while heap:
            sdist, sNode = heapq.heappop(heap)
            if visited[sNode] == 1:
                continue
            
            visited[sNode] = 1
            for node, prob in adjMat[sNode]:
                
                if node == sNode or visited[node] == 1:
                    continue
                # print(sNode,"---", node, prob, dist[sNode], dist[sNode] * prob)
                if dist[node] < dist[sNode] * prob:
                    dist[node] = dist[sNode] * prob
                    heapq.heappush(heap, (-1*dist[node], node))
        
        # print(dist)
        return dist[end] if dist[end] != float('-inf') else 0
        
        
            
        
        
        