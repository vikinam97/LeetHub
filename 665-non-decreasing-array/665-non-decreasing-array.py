class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if i == 1:
                    count += 1
                else:
                    # j = i-2
                    # while j >= 0:
                    #     if nums[j] > nums[i] and i < len(nums) - 1 and nums[j+1] > nums[i+1]:
                    #         return False
                    #     j -= 1
                    if nums[i-2] > nums[i] and i < len(nums) - 1 and nums[i-1] > nums[i+1]:
                        return False
                    count += 1
            
            if count > 1:
                return False
        
        return True