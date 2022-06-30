class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        
        steps = 0
        for i in range(len(nums)):
            steps += abs(nums[i] - median)
            
        return steps
        
#         avg = int(sum(nums) / len(nums))
        
#         steps = 0
#         diff, closeSoFar = float('inf'), float('inf')
#         for i in range(len(nums)):
#             tempDiff = abs(nums[i] - avg)
#             if diff > tempDiff:
#                 diff = tempDiff
#                 closeSoFar = nums[i]
        
#         for i in range(len(nums)):
#             steps += abs(nums[i] - closeSoFar)
            
#         return steps