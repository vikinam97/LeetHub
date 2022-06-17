class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # Solution - 2 set binary serach
        # Time - O(2^(N/2) * log(2^(N/2))
        # Space O(2^n)
        def generateSubsetSumList(st, ed):
            result = [0]
            for i in range(st, ed+1):
                prevLen = len(result)
                for j in range(prevLen):
                    result.append(result[j] + nums[i])
            return result
        
        list1 = generateSubsetSumList(0, (len(nums)) // 2)
        list2 = generateSubsetSumList((len(nums)) // 2 + 1, len(nums) - 1)
        
        list2.sort()
        
        closeSoFar = float('infinity')
        result = float('infinity')
        
        for i in range(len(list1)):
            subTarget = goal - list1[i]
            i = bisect_left(list2, subTarget)
            
            if i < len(list2):
                closeSoFar = min(closeSoFar, abs(subTarget - list2[i]))
                
            if i > 0:
                closeSoFar = min(closeSoFar, abs(subTarget - list2[i-1]))
        
        return closeSoFar
            
        
        