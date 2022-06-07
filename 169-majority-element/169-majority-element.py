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