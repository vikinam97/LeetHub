class HeapNode:
    def __init__(self, weight, val):
        self.weight = weight
        self.val = val
    
    def __lt__(self, other):
        return self.weight < other.weight 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        j = 0
        
        result = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, HeapNode(-1 * nums[i], i))
            
            if (i - j + 1) > k:
                j += 1
                
            while maxHeap and maxHeap[0].val < j:
                a = heapq.heappop(maxHeap)
                
#             # for z in range(len(maxHeap)):
#             #     print(maxHeap[z].weight, maxHeap[z].val)
                
            if (i - j + 1) == k:
                result.append(-1 * maxHeap[0].weight)
                
        return result
        