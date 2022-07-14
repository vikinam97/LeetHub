class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums) - 1
        
        # for l == r on [1] arr
        while l <= r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while r > l and nums[r] == nums[r-1]:
                r -= 1
            
            mid = l + ((r - l) // 2)
            
            if nums[mid] == target:
                return True
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return False
                
            
                    
        
                
        