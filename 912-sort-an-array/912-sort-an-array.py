class Solution(object):
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, start, end):
        if end <= start:
            return
        mid = (start + end) // 2
        nums[start], nums[mid] = nums[mid], nums[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]        
        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j-1)
        self.quickSort(nums, j+1, end)

