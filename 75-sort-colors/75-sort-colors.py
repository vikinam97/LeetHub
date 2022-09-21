class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Solution - 3 pointer
        # Time - O(N)
        # Space - O(1)
        
        i, j, k = 0, len(nums)-1, 0
        
        while k <= j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1
                
        return nums
            
            
        