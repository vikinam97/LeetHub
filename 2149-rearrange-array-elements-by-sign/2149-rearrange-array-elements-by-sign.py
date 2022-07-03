class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        negs = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                negs.append(nums[i])
        
        pos.reverse()
        negs.reverse()
        result = []
        while pos and negs:
            result.append(pos.pop())
            result.append(negs.pop())
        
        return result
        