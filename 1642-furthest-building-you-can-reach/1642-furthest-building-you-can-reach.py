class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        heapq.heapify(heap)
        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(heap, -diff)
                else:
                    if ladders == 0:
                        return i - 1
                    else:
                        maximum = -heapq.heappushpop(heap, -diff)
                        bricks += maximum - diff
                        ladders -= 1
        return n - 1

# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         heap = []
        
#         for i in range(len(heights) - 1):
#             diff = heights[i + 1] - heights[i]
            

            
#             if diff <= 0:
#                 continue
            
#             bricks -= diff
#             heapq.heappush(heap, -1 * diff)
#             print(diff, bricks, heap)
            
#             if bricks <= 0:
#                 if heap and ladders > 0:
#                     lastMaxBricksUsed = -1 * heapq.heappop(heap)
#                     bricks += lastMaxBricksUsed
#                     ladders -= 1
#                     continue
            
#             if bricks <= 0 and ladders <= 0:
#                 return i
        
#         return len(heights) - 1 
                

                    
                    
                
        