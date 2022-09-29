from heapq import heappop, heappush, heapify

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        heap = [ (abs(a-x), i, a) for i, a in enumerate(arr)]
        
        heapify(heap)
        result = []
        
        while heap and k > 0:
            result.append(heappop(heap)[2])
            k -= 1
        
        result.sort()
        
        return result
        
        
        