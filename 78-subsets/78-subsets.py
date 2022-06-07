class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 2 using array
        superSet = [[]]
        
        for num in nums:
            setLen = len(superSet)
            for idx in range(setLen):
                temp = superSet[idx][:]
                temp.append(num)
                superSet.append(temp)
        
        return superSet
        
        
        # Solution 1 -- using bit manipulation
        # Time -> O(N * 2 ^ N)
        # Space -> O(2 ^ N)
        # superSet = []
        # for i in range(pow(2, len(nums))):
        #     subSet = []
        #     for bit in range(len(nums)):
        #         if i & (1 << bit):
        #             subSet.append(nums[bit])
        #     superSet.append(subSet)
        # return superSet
                
            