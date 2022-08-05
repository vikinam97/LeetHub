class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pLen = len(points)
        adjMat = [[0]*pLen for i in range(pLen)]
        
        for i in range(pLen):
            x1, y1 = points[i]
            for j in range(pLen):
                if i == j:
                    adjMat[i][j] = 0
                    continue
                x2, y2 = points[j]
                adjMat[i][j] = abs(x1 - x2) + abs(y1 - y2)
            
        
        dist = [float('inf')] * pLen
        visited = [-1] * pLen
        dist[0] = 0
        
        heap = [(0, 0)]
        
        while heap:
            # print("--")
            wt, point = heapq.heappop(heap)
            if visited[point] == 1:
                continue
            visited[point] = 1
            for i in range(pLen):
                if visited[i] == 1:
                    continue
                dist[i] = min(dist[i], adjMat[point][i]) 
                heapq.heappush(heap, (dist[i], i))
        # print(visited)
        # print(dist)
        return sum(dist)
            
        
        