class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Solution - process simulation
        # Time - O(N^2)
        # Space - O(N)
        
        for i in range(1, len(nums)):
            for j in range(len(nums)-i):
                nums[j] += nums[j+1]
                if nums[j] >= 10:
                    nums[j] = nums[j] % 10
            
        return nums[0]