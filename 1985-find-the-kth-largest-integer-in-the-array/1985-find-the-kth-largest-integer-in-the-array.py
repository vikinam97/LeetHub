class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x:int(x))
        print(nums)
        return nums[len(nums) - k]