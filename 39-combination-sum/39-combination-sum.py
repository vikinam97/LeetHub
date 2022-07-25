class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution - backtrack
        # Time - O(N^M)
        #     - N = no of cands
        #     - M = target (worst case cands 1 so max M call stack)
        # Space - O(N^M)
        
        self.comboResult = []
        candidates.sort()
        self.backtrack(0, [], candidates, target)
        return self.comboResult
    
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
        