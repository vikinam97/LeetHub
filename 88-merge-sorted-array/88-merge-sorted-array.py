class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1[:m]
        nums1.clear()
        
        i, j = 0, 0
        while i < m and j < n:
            if nums1Copy[i] < nums2[j]:
                nums1.append(nums1Copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
                
        while i < m:
            nums1.append(nums1Copy[i])
            i += 1
        
        while j < n:
            nums1.append(nums2[j])
            j += 1
            
        
        