class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Solution - deque
        # Time - O(N)
        # Space - O(N)
        if not nums:
            return None
        
        q = collections.deque([(nums[0],0)])
        
        for i in range(1, len(nums)):
            
            while q and q[0][1] < i - k:
                q.popleft()
            
            curScore = q[0][0] + nums[i]

            while q and q[-1][0] < curScore:
                q.pop()
            
            q.append((curScore, i))
        
        return q[-1][0]
                 
class Solution1:
    def maxResult(self, nums: List[int], k: int) -> int:        
        # Solution  - Brute force checking on max sub sequence
        # Time - O(N^2)
        # Space - O(N)
        if not nums:
            return -1
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            maxInRange = float('-inf')
            for j in range(max(0, i-k), i):
                maxInRange = max(maxInRange, dp[j])
            
            dp[i] += nums[i] + maxInRange
        
        return dp[-1]
            
        
        
                
        