class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = 0;
        result = nums[0]
        for i in nums:
            currentMax = max(i, i + currentMax)
            if currentMax > result:
                result = currentMax
        return result

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = 0;
        result = nums[0]
        for i in nums:
            if currentMax < 0:
                currentMax = 0
            currentMax += i;
            result = max(currentMax, result)
        return result