class Solution:
    def radixSort(self, nums):
        # Solution - Radix sort
        # Time - O(log(max(N)) * ( R + N ) ) 
        #     R -> range of input
        #     N -> array
        # Space - (R + N)
        def countingSortByDigit(nums, digit):
            div = pow(10, digit)
            result = [0] * len(nums)
            rangeArray = [0] * 10
            
            for i in range(len(nums)):
                d = math.trunc(nums[i] / div) % 10 
                rangeArray[d] += 1
            
            for i in range(1, len(rangeArray)):
                rangeArray[i] = rangeArray[i-1] + rangeArray[i]
            
            for i in range(len(nums) -1, -1 ,-1):
                d = math.trunc(nums[i] / div) % 10
                idx = rangeArray[d]
                result[idx - 1] = nums[i]
                rangeArray[d] -= 1
            
            return result 
            
        
        maxinList = max(nums)
        
        # count nof digits
        digitCount = 0
        while maxinList != 0:
            digitCount += 1
            maxinList = math.trunc(maxinList / 10)
        
        for i in range(digitCount):
            nums = countingSortByDigit(nums, i)
            
        return nums
    
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        # nums = self.radixSort(nums);
        nums.sort()
        diff = 0
        for i in range(len(nums)-1):
            diff = max(diff, nums[i+1] - nums[i])
        
        return diff
        
        
