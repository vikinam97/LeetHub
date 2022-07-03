class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Solution - division of array
        # Time - O(N)
        # Space - O(N)
        pos = []
        negs = []
        i = len(nums) - 1
        while i>=0:
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                negs.append(nums[i])
            i -= 1
        
        # pos.reverse()
        # negs.reverse()
        result = []
        while pos and negs:
            result.append(pos.pop())
            result.append(negs.pop())
        
        return result
        