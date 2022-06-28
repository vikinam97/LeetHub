class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        deletedCount = 0
        for i in range(len(nums)-1):
            idx = i - deletedCount
            if (idx & 1 == 0) and nums[i] != nums[i+1]:
                stack.append(nums[i])
            elif (idx & 1 == 1):
                stack.append(nums[i])
            else:
                deletedCount += 1
        stack.append(nums[-1])
        
        if len(stack) & 1 == 1:
            deletedCount += 1
        
        return deletedCount
                