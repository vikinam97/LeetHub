class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, j, k = [], [], []
        for h in range(len(nums)):
            if nums[h] < pivot:
                i.append(nums[h])
            elif nums[h] > pivot:
                j.append(nums[h])
            else:
                k.append(nums[h])
        
        return i + k + j
            
            
            
            
            
            
            
            
            
            
        