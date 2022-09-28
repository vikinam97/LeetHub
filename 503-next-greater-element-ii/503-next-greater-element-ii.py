class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        nxtGrt = [-1] * len(nums)
        
        i = 0
        while i < len(nums):
            
            while stack and stack[-1][0] < nums[i]:
                val, idx = stack.pop()
                nxtGrt[idx] = nums[i]
            
            stack.append([nums[i], i])
        
            i += 1
            
        i = 0
        while i < len(nums):
            
            while stack and stack[-1][0] < nums[i]:
                val, idx = stack.pop()
                nxtGrt[idx] = nums[i]
            
            stack.append([nums[i], i])
        
            i += 1
        
        return nxtGrt
        