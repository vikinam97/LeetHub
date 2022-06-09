class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 2
        
        i, j = 0, len(numbers) - 1
        while i < j:
            tempSum = numbers[i] + numbers[j]
            if tempSum == target:
                return [i+1, j+1]
            elif tempSum > target:
                j -= 1
            else:
                i += 1
        return None
                
        
        # Solution 1
        # Time O(NlogN)
        # Space O(1)
#         def binarySearch(idx, subTarget):
#             i, j = idx + 1, len(numbers) - 1
#             while i <= j:
#                 mid = (i + j) // 2
#                 print(i, j, mid);

#                 if numbers[mid] == subTarget:
#                     return mid
#                 elif numbers[mid] > subTarget:
#                     j = mid - 1
#                 else:
#                     i = mid + 1
#             return None
        
#         for i in range(len(numbers)):
#             subTarget = target - numbers[i]
#             tempNumIdx = binarySearch(i, subTarget)
#             if tempNumIdx != None and numbers[tempNumIdx] == subTarget:
#                 return [i+1, tempNumIdx+1]
            
#         return None
            