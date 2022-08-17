class Solution:

    def recur(self, idx, i, target, nums):
        if idx >= len(nums):
            return i == target
        
        if (idx, i) in self.memo:
            return self.memo[(idx, i)]
        
        self.memo[(idx, i)] = (self.recur(idx+1, i + nums[idx], target, nums) or
                              self.recur(idx+1, i, target, nums))
        
        return self.memo[(idx, i)]
            
    def canPartition(self, nums: List[int]) -> bool:
        self.memo = {}
        
        target = sum(nums)/2
        
        if target != int(target):
            return False
        
        return self.recur(0, 0, int(target), nums)
        