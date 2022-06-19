class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Solution - prefix sum
        # Time O(N)
        # Space O(1)
        total = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (total - leftsum - x):
                return i
            leftsum += x
        return -1
        
        # Solution - prefix and suffix sum
        # Time O(N)
        # Space O(N)
        # leftSum = [0] * len(nums)
        # rightSum = [0] * len(nums)
        # leftSum[0] = nums[0]
        # rightSum[len(nums)-1] = nums[len(nums)-1]
        # lth = len(nums)
        # for i in range(lth-2, -1, -1):
        #     rightSum[i] = rightSum[i+1] + nums[i]
        # for i in range(lth):
        #     leftSum[i] = leftSum[i-1] + nums[i]
        #     if leftSum[i] == rightSum[i]:
        #         return i
        # return -1