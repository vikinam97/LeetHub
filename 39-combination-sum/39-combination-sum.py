class Solution:
    def backtrack(self, pathSum, path, cand, tar):
        if pathSum > tar:
            return
        
        if pathSum == tar:
            self.comboResult.append(path[:])
            return
        
        for idx, num in enumerate(cand):
            path.append(num)
            self.backtrack(pathSum + num, path, cand[idx:], tar)
            path.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.comboResult = []
        candidates.sort()
        self.backtrack(0, [], candidates, target)
        return self.comboResult

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         ret = []
#         self.dfs(candidates, target, [], ret)
#         return ret
    
#     def dfs(self, nums, target, path, ret):
#         if target < 0:
#             return 
#         if target == 0:
#             ret.append(path)
#             return 
#         for i in range(len(nums)):
#             self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)