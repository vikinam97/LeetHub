class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using bit XOR nad AND
        
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones

        # Bit Masking
#         singleNumber = 0
#         for i in range(32):
#             setBitCount = 0
#             shiftedNumber = 1 << i
#             for num in nums:
#                 if num & shiftedNumber:
#                     setBitCount += 1
#             if setBitCount % 3 != 0:
#                 singleNumber = singleNumber | shiftedNumber
            
#         return singleNumber

                