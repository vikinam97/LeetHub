# Time -> O(n)
# Space -> O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorOfAll = 0;
        for num in nums:
            xorOfAll = xorOfAll ^ num
        
        firstSetBit = 0
        while (xorOfAll & ( 1 << firstSetBit)) == 0:
            firstSetBit += 1
        
        bitMask = 1 << firstSetBit
        firstNumber, secondNumber = 0, 0
        for num in nums:
            if bitMask & num:
                firstNumber ^= num
            else: 
                secondNumber ^= num
                
        return [firstNumber, secondNumber]
            
            
            