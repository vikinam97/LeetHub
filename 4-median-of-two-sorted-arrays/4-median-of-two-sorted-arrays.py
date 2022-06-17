class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 = [*nums1, *nums2]
        
        nums1.sort()
        
        mid = (len(nums1)-1) // 2
        
        if len(nums1) & 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid+1]) / 2
