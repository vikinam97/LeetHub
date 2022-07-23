class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        #a = SortedList()
        a = []
        ans = []
        
        for v in nums[::-1]:
            ans.append(bisect.bisect_left(a, v))
            bisect.insort(a, v)
        
        return ans[::-1]