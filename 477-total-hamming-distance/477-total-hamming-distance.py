class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Solution 2
        totalSoFar = 0
        for i in range(32):
            setBitCount = 0
            for num in nums:
                if num & (1 << i):
                    setBitCount += 1
            totalSoFar += setBitCount * (len(nums) - setBitCount)
        
        return totalSoFar
        
        
        # Solution 1
        # Time O(N ^ 2 * 32)
        # Space O(1)
#         def calculateHamming(num1, num2):
#             temp = num1 ^ num2
#             count = 0
#             while temp != 0:
#                 count += 1
#                 temp = temp & (temp - 1)
#             return count
        
#         totalSoFar = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 totalSoFar += calculateHamming(nums[i], nums[j])
            
#         return totalSoFar