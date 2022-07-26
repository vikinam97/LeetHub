class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Solution - all combo
        # Time - O(N!)
        # Space - O(N!)
        
        self.perList = []
        self.recur(nums, [], [0] * len(nums))
        return self.perList
    
    def recur(self, nums, path, used):
        if len(path) == len(nums):
            self.perList.append(path[:])
            return
        
        for idx, num in enumerate(nums):
            if used[idx] == 0:
                used[idx] = 1
                path.append(num)
                self.recur(nums, path, used)
                path.pop()
                used[idx] = 0
        