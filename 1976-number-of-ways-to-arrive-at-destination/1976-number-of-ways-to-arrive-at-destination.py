
MOD = (10**9) + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjMat = defaultdict(list)
        
        for u, v, dist in roads:
            adjMat[u].append((v, dist))
            adjMat[v].append((u, dist))
        
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [0] * n
        
        ways = [0] * n
        ways[0] = 1
        
        heap = [(0, 0)] # (distance, vertex)
        
        while heap:
            distance, node = heapq.heappop(heap)
                        
            for adj, dv in adjMat[node]:
                if dv + distance < dist[adj]:
                    dist[adj] = dv + distance
                    heapq.heappush(heap, (dv + distance, adj))
                    ways[adj] = ways[node]
                elif dist[adj] == dv + distance:
                    ways[adj] += ways[node]

        return ways[n-1] % MOD
        