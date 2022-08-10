class Solution:
    def canJump(self, nums):
        max_index = 0     # max index achieved
        for i, j in enumerate(nums):
            max_index = max(i+j, max_index)
            if max_index >= len(nums)-1: return True
            if max_index == i: return False
        
            