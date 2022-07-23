class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]
        
        result = [0]*n
        
        def merge_sort(arr, left, right):
            if left >= right:
                return 
            mid = left + (right-left)//2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid+1, right)
            merge(arr, left, mid, mid+1, right)
            
        
        def merge(arr, ls, le, hs, he):
            i = ls
            j = hs
            temp = []
            rightcount = 0
            
            while i <= le and j <= he:
                if arr[j][0] < arr[i][0]:
                    rightcount += 1
                    temp.append(arr[j])
                    j += 1
                else:
                    result[arr[i][1]] += rightcount
                    temp.append(arr[i])
                    i += 1
            
            while i <= le:
                result[arr[i][1]] += rightcount
                temp.append(arr[i])
                i += 1
            
            while j <= he:
                temp.append(arr[j])
                j += 1
            
            
            arr[ls:he+1] = temp
            
        
        merge_sort(arr, 0, n-1)
        return result