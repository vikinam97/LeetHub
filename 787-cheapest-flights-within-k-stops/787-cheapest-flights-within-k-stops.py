class Solution:
    
    def genAdjList(self, flights, n):
        adjList = [[] for i in range(n)]
        for u, v, cost in flights:
            adjList[u].append((v, cost))
        return adjList
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjList = self.genAdjList(flights, n)
        
        costList = [float('inf')] * n
        costList[src] = 0
        visited = [-1] * n
        
        heap = [(0, 0, src)]
        
        foundPathCost = float('inf')
        
        while heap:
            lev, curr_p, node= heapq.heappop(heap)
            if lev == k + 1 and node == dst:
                costList[dst] = min(costList[dst], curr_p)
                
            if lev < k + 1:
                if node == dst:
                    costList[dst] = min(costList[dst], curr_p)
                
                for nei, pri in adjList[node]:
                    if costList[nei] > curr_p + pri:
                        costList[nei] = curr_p + pri
                        heapq.heappush(heap, [lev + 1, curr_p + pri, nei])
                        
        print(costList)
        return costList[dst] if costList[dst] != float("inf") else -1