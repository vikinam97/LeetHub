class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        def generateSubsetSumList(st, ed):
            result = [0]
            for i in range(st, ed+1):
                prevLen = len(result)
                for j in range(prevLen):
                    result.append(result[j] + nums[i])
            return result
        
#         def searchBinary(arr, target):
#             l, r = 0, len(arr) - 1
#             while l < r:
#                 mid = (l + r) // 2
                
#                 if arr[mid] == target:
#                     return arr[mid]
#                 elif arr[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
            
#             return arr[l]
        
        list1 = generateSubsetSumList(0, (len(nums)) // 2)
        list2 = generateSubsetSumList((len(nums)) // 2 + 1, len(nums) - 1)
        
        list2.sort()
        
        closeSoFar = float('infinity')
        result = float('infinity')
        
        for i in range(len(list1)):
            t = goal - list1[i]
            i = bisect_left(list2, t)
            
            if i < len(list2):
                result = min(result, abs(t - list2[i]))
                
            if i > 0:
                result = min(result, abs(t - list2[i-1]))
            
            
#             subTarget = goal - list1[i]
#             ps = searchBinary(list2, subTarget)
#             print(list1[i], subTarget, ps)
            
#             diff = abs(goal - (ps + list1[i]))
#             if diff == 0:
#                 return 0
#             closeSoFar = min(closeSoFar, diff)
        
        return result
            
        
        