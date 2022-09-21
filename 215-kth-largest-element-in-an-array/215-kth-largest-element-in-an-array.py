class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = []
        
        for i in range(len(nums)):
            
            heapq.heappush(minHeap, nums[i])
            
            while len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return minHeap[0]