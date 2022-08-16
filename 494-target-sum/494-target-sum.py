class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Solution - recursion memoization
        # Time - O(N*2)
        # Space - O(N*2)
        
        self.memo = {}
        return self.recur(0, 0, nums, target)
    
    def recur(self, i, curSum, nums, target):
        if i >= len(nums):
            return 1 if curSum == target else 0
        
        if (i, curSum) in self.memo:
            return self.memo[(i, curSum)]
        
        self.memo[(i, curSum)] = (self.recur(i+1, curSum + nums[i], nums, target) + 
                self.recur(i+1, curSum - nums[i], nums, target))
    
        return self.memo[(i, curSum)]
        