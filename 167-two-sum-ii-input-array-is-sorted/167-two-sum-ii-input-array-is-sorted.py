class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binarySearch(idx, subTarget):
            i, j = idx + 1, len(numbers) - 1
            while i <= j:
                mid = (i + j) // 2
                print(i, j, mid);

                if numbers[mid] == subTarget:
                    return mid
                elif numbers[mid] > subTarget:
                    j = mid - 1
                else:
                    i = mid + 1
            return None
        
        for i in range(len(numbers)):
            tempNumIdx = binarySearch(i, target - numbers[i])
            if tempNumIdx != None and numbers[tempNumIdx] == (target - numbers[i]):
                return [i+1, tempNumIdx+1]
            
        return None
            