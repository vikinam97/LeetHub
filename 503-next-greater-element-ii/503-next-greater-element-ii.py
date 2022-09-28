class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        def traverseNextGreat():
            i = 0
            while i < len(nums):

                while stack and stack[-1][0] < nums[i]:
                    val, idx = stack.pop()
                    nxtGrt[idx] = nums[i]

                stack.append([nums[i], i])

                i += 1
                
        stack = []
        nxtGrt = [-1] * len(nums)
        
        traverseNextGreat()
        traverseNextGreat()
        
        return nxtGrt
        