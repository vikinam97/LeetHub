class NumArray:
    # Solution - prefix sum
    # Time - O(N + Q) Q = number of query
    # Space - O(N)
    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)
        self.prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefixSum[left-1] if left > 0 else 0 
        return self.prefixSum[right] - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)