class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numHash = defaultdict(int)
        slidingSum, maxSum = 0, 0
        i, j = 0, 0
        
        for j in range(len(nums)):
            num = nums[j]
            numHash[num] += 1
            slidingSum += num
            
            while i < j and numHash[num] > 1:
                slidingSum -= nums[i]
                numHash[nums[i]] -= 1
                i += 1
            
            maxSum = max(maxSum, slidingSum)
            
        return maxSum