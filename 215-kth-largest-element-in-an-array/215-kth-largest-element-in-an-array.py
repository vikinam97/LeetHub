class Solution:
    
    def partition(self, start, end, nums, k):
        # Solution - Quick Select
        # Time - O(N*N) worst - avg O(N)
        # Space - O(1)
        
        if start >= end:
            return nums[start]
        
        i, j, pivot = start, end, end
        
        while i < j:
            if nums[i] < nums[pivot]:
                i += 1
                continue
            if nums[j] >= nums[pivot]:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i], nums[pivot] = nums[pivot], nums[i]
        
        if i < len(nums) - k:
            return self.partition(i+1, end, nums, k)
        elif i > len(nums) - k:
            return self.partition(start, i-1, nums, k)
        
        return nums[i]     
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.partition(0, len(nums)-1, nums, k)
    
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution - Heap
        # Time - O(NlogK)
        # Space - O(K)
        
        minHeap = []
        
        for i in range(len(nums)):
            heapq.heappush(minHeap, nums[i])
            
            while len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return minHeap[0]
    

