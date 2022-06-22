class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def countSort(digit):
            count = [0] * 10
            res = [0] * len(nums)
            
            # counting of how many numbers have the digit-th equal to 0-9
            for num in nums:
                count[(num // (10 ** digit)) % 10] += 1
                
            for i in range(1, 10):
                count[i] += count[i - 1] # define the index of each bucket
                
            count = [0] + count
            
            for num in nums:
                idx = (num // (10 ** digit)) % 10
                res[count[idx]] = num
                count[idx] += 1
            
            for i in range(len(nums)):
                nums[i] = res[i]
                
        if not nums or len(nums) < 2:
            return 0
        
        # define maximum number of digits
        maxValue = max(nums)
        maxDigits = 0
        while maxValue > 0:
            maxDigits += 1
            maxValue //= 10
        # Radix-Sort: sort the array in O(n) with aid of count sort for each digit
        for digit in range(maxDigits):
            countSort(digit)
            digit += 1
            
        # calculate the max diff between two successive elements in sorted array
        maxDiff = -float('inf')
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, abs(nums[i] - nums[i-1]))
        return maxDiff

# class Solution:
#     def radixSort(self, nums):
#         # Solution - Radix sort
#         # Time - O(log(max(N)) * ( R + N ) ) 
#         #     R -> range of input
#         #     N -> array
#         # Space - (R + N)
#         def countingSortByDigit(nums, digit):
#             div = pow(10, digit)
#             result = [0] * len(nums)
#             rangeArray = [0] * (max(nums) + 1)
            
#             for i in range(len(nums)):
#                 d = math.trunc(nums[i] / div) % 10 
#                 rangeArray[d] += 1
            
#             for i in range(1, len(rangeArray)):
#                 rangeArray[i] = rangeArray[i-1] + rangeArray[i]
            
#             for i in range(len(nums) -1, -1 ,-1):
#                 d = math.trunc(nums[i] / div) % 10
#                 idx = rangeArray[d]
#                 result[idx - 1] = nums[i]
#                 rangeArray[d] -= 1
            
#             return result 
            
        
#         maxinList = max(nums)
        
#         # count nof digits
#         digitCount = 0
#         while maxinList != 0:
#             digitCount += 1
#             maxinList = math.trunc(maxinList / 10)
        
#         for i in range(digitCount):
#             nums = countingSortByDigit(nums, i)
            
#         return nums
    
#     def maximumGap(self, nums: List[int]) -> int:
        
#         if len(nums) < 2:
#             return 0
        
#         nums = self.radixSort(nums);
#         # nums.sort()
#         diff = 0
#         for i in range(len(nums)-1):
#             diff = max(diff, nums[i+1] - nums[i])
        
#         return diff
        
        
