class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if i == 1:
                    count += 1
                else:
                    if nums[i-2] > nums[i] and i < len(nums) - 1 and nums[i-1] > nums[i+1]:
                        return False
                    count += 1
            
            if count > 1:
                return False
        
        return True