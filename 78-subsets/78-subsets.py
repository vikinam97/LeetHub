class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 -- using bit manipulation
        superSet = []
        for i in range(pow(2, len(nums))):
            subSet = []
            for bit in range(len(nums)):
                if i & (1 << bit):
                    subSet.append(nums[bit])
            superSet.append(subSet)
            
        return superSet
                
            