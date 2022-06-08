class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xorToN(n):
            mod = n % 4
            if mod == 1:
                return 1
            if mod == 2:
                return n + 1
            if mod == 3:
                return 0
            return n
        
        xorAllN = xorToN(len(nums))
        
        xorNums = 0
        for num in nums:
            xorNums = xorNums ^ num
            
        return xorNums ^ xorAllN