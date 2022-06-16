class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        lastPeak = -1
        for i in range(len(nums)):
            if nums[i] > nums[i-1]:
                lastPeak = i
        
        if lastPeak == -1:
            return nums.sort()
        
        # to check the min element after last peak
        tempPeak = lastPeak
        for i in range(lastPeak, len(nums)):
            if nums[i] > nums[lastPeak-1] and nums[i] < nums[tempPeak]:
                tempPeak = i
        
        
        # swap peak to last min
        nums[lastPeak-1], nums[tempPeak] = nums[tempPeak], nums[lastPeak-1]
        
        # sort the sub array
        l = nums[lastPeak:]
        l.sort()
        nums[lastPeak:] = l
        