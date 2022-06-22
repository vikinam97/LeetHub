class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(start, end):
            if start >= end:
                return nums[start]
            
            i = start - 1
            j = start
            pivot = end
            
            while j < end:
                if nums[j] < nums[pivot]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                else:
                    j += 1
            
            nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
            if (i+1) == (len(nums) - k):
                return nums[i + 1]
            
            if (i+1) > (len(nums) - k):
                return partition(start, i)
            
            return partition(i+2, end)
        
        return partition(0, len(nums)-1)
        