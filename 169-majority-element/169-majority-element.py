class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moores voting algorith find majority over n/2         
        meSoFar, count = None, 1
        
        for num in nums:
            if meSoFar != num:
                count -= 1
            else: 
                count += 1
                
            if count == 0:
                meSoFar = num
                count = 1
            
        return meSoFar

        # Bit masking algo -> bit set if no of bits is > n/2
#         majElement = 0
#         for i in range(32):
#             setBitCount = 0
#             for num in nums:
#                 if (num & (1 << i)):
#                     setBitCount += 1
#             if setBitCount > (len(nums)/2):
#                 majElement = majElement | (1 << i)
                
#         return majElement
                
                