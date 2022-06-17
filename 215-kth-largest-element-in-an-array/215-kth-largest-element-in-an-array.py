class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution - Quick Select Algo
        # Time - O(N)
        # Space - O(log(k)) recursive stack
        
        def partition(start, end):
            i, j = start, end
            pivot = end
            
            while i < j:
                if nums[i] < nums[pivot]:
                    i += 1
                    continue
                if nums[j] >= nums[pivot]:
                    j -= 1
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                
            nums[i], nums[pivot] = nums[pivot], nums[i]
            
            # selecting next apth
            if i == len(nums) - k:
                return nums[i]
            elif i > len(nums) - k:
                return partition(start, i-1)
            
            return partition(i+1, end)
        return partition(0, len(nums) -1)
        