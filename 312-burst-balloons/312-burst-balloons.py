class Solution:
    def maxCoins(self, nums):
        # Solution - Dynamic Programming - Tabulation
        # Time - O(N*N*N)
        # Space - O(N*N)
        
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)]
        
        for i in reversed(range(1, n+1)):
            for j in range(1, n+1):
                if i > j: continue
                    
                maxi = float('-inf')
                for k in range(i, j+1):
                    cost = ((nums[i-1] * nums[k] * nums[j+1]) + 
                           dp[i][k-1] + dp[k+1][j])
                    maxi = max(maxi, cost)
                
                dp[i][j] = maxi
        
        return dp[1][n]
                    
    
class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        # Solution - Recusion + Memoization - TLE leetcode
        # Time - O(N*N*N)
        # Space - O(N*N)
        
        self.memo = {}
        return self.recur(1, len(nums), [1] + nums + [1])
    
    def recur(self, i, j, nums):
        if i > j: return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        cost = float('-inf')
        
        for k in range(i, j+1):
            cost = max(cost, (nums[i-1] * nums[k] * nums[j+1]) +
                   self.recur(i, k-1, nums) +
                   self.recur(k+1, j, nums)) 
            
        self.memo[(i, j)] = cost
        return cost
        