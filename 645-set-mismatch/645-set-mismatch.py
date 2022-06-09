class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = None
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] < 0:
                dup = num
            else: 
                nums[num-1] = nums[num-1] * -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                return [dup, i+1]
        
        return None
            
        