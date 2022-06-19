class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        
        leftSum[0] = nums[0]
        rightSum[len(nums)-1] = nums[len(nums)-1]
        lth = len(nums)
        for i in range(lth-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i]
        for i in range(lth):
            leftSum[i] = leftSum[i-1] + nums[i]
            if leftSum[i] == rightSum[i]:
                return i
        
        
        return -1