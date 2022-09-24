class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        nums.append(-1)
        stack = [[-1, -1]]
        
        result = 0
        
        for i in range(len(nums)):
            
            while stack and stack[-1][0] > nums[i]:
                val, idx = stack.pop()
                right = i-idx
                left = idx - (stack[-1][1] if stack else -1)
                
                cont = val * left * right
                result += cont
            
            stack.append([nums[i], i])
        
        return result % (10**9 + 7)
                
    
    