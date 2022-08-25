class Solution:
    def maxCoins(self, nums):
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range(0, n - d):
                j = i + d
                for k in range(i + 1, j):
                    last_burn = nums[i] * nums[k] * nums[j]
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + last_burn)
        return dp[0][n - 1]
#     def recur(self, i, j, nums):
#         if i > j: return 0
        
#         if (i, j) in self.memo:
#             return self.memo[(i, j)]
        
#         cost = float('-inf')
        
#         for k in range(i, j+1):
#             cost = max(cost, (nums[i-1] * nums[k] * nums[j+1]) +
#                    self.recur(i, k-1, nums) +
#                    self.recur(k+1, j, nums)) 
            
#         self.memo[(i, j)] = cost
#         return cost
    
#     def maxCoins(self, nums: List[int]) -> int:
#         self.memo = {}
#         return self.recur(1, len(nums), [1] + nums + [1])
        