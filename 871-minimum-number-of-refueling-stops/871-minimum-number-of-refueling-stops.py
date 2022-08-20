class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Solution - Greedy 
        # Time - O(NlogN)
        # Space - O(N)
        
        if not stations:
            return 0 if target <= startFuel else -1
        
        heap = []
        stations.append([target, float('inf')])
        
        tank, count, last = startFuel, 0, 0
        
        for pos, fuel in stations:
            tank = tank - (pos - last)
            
            while heap and tank < 0:
                tank += -1 * heapq.heappop(heap)
                count += 1
            
            if tank < 0:
                return -1
            
            heapq.heappush(heap, -1 * fuel)
            last = pos
            
        return count
            
            
        