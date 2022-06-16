class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        print(hashMap)
        for i in range(len(nums)):
            if (target - nums[i]) in hashMap and hashMap[target - nums[i]] != i:
                return [i, hashMap[target - nums[i]]]
        return []