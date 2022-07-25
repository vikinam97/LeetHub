# class Solution:
#     def backtrack(self, pathSum, path, cand, tar, seen, seenPath):
#         if pathSum > tar:
#             return
        
#         if pathSum == tar:
#             pathStr = "".join([str(fre) for fre in seen])
#             if pathStr not in seenPath:
#                 self.comboResult.append(path[:])
#                 seenPath[pathStr] = True
#             return
        
#         for idx, num in enumerate(cand):
#             path.append(num)
#             seen[idx] += 1
#             self.backtrack(pathSum + num, path, cand, tar, seen, seenPath)
#             seen[idx] -= 1
#             path.pop()
    
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.comboResult = []
#         candidates.sort()
#         self.backtrack(0, [], candidates, target, [0]*len(candidates), {})
#         return self.comboResult

class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)