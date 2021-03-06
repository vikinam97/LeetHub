class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        deletedCount = 0
        for i in range(len(nums)-1):
            idx = i - deletedCount
            if idx & 1 == 0 and nums[i] == nums[i+1]:
                deletedCount += 1
        
        if (len(nums) - deletedCount) & 1 == 1:
            deletedCount += 1
        
        return deletedCount
                