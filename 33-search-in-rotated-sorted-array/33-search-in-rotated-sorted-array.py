class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
    
    
    
    def binary_search(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (start+end)//2
        
        if nums[mid] == target:
            return mid
        
        
        # start to mid is sorted
        if nums[start] <= nums[mid]:
            if nums[start]<=target<nums[mid]:
                return self.binary_search(nums, start, mid-1, target)
            else:
                return self.binary_search(nums, mid+1, end, target)
        # mid to end is sorted
        else:
            if nums[mid]<target<=nums[end]:
                return self.binary_search(nums, mid+1, end, target)
            else:
                return self.binary_search(nums, start, mid-1, target)
            
#     def search(self, nums: List[int], target: int) -> int:
#         # step1 find the break point using binary search
#         l, r = 0, len(nums) - 1
#         breakpoint = len(nums) - 1
#         while l <= r:
#             mid = (r + l) // 2
#             if (mid < r and nums[mid + 1] < nums[mid]) or (mid > 0 and nums[mid - 1] > nums[mid]):
#                 breakpoint = mid
#                 break
#             elif nums[mid] > nums[l]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         print(breakpoint)
        
#         # find the nums in segement
#         if nums[0] < target < nums[breakpoint]:
#             l, r = 0, breakpoint 
#         else: 
#             l, r = breakpoint + 1, len(nums) - 1
        
#         print(nums[l:r+1])
#         while l <= r:
#             mid = (r + l) // 2
#             # print(l, r, mid)
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 l = mid + 1 
#             else:
#                 r = mid - 1
        
#         return -1
        
        
            
        