class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                evenSum += nums[i]
        
        result = []
        
        for val, idx in queries:
            sm = nums[idx] + val
            
            if nums[idx] & 1 and sm & 1 == 0:
                evenSum += sm
            elif nums[idx] & 1 == 0 and sm & 1:
                evenSum -= nums[idx]
            elif nums[idx] & 1 == 0 and sm & 1 == 0:
                evenSum = evenSum - nums[idx] + sm
                
            nums[idx] = sm
            result.append(evenSum)
                
        return result
        