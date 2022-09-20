class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length=len(nums)
        left, right, result= [0]*length, [0]*length, [0]*length
        
        runningProduct = 1
        
        for i in range(length):
            left[i] = runningProduct
            runningProduct *= nums[i]
        
        runningProduct = 1
        
        for j in reversed(range(length)):
            right[j] = runningProduct
            runningProduct *= nums[j]
        
        for i in range(length):
            result[i] = left[i] * right[i]
        
        return result
        
        
           