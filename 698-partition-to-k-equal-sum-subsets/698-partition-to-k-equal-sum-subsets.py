class Solution:
    def canPartitionKSubsets(self, A, k):
        n, val = len(A), sum(A) / k
        if val != floor(val):
            return False
        A.sort()
        def btrack(i, space, k):
            if k == 1: return True
            for j in range(i, n):
                if val >= A[j] > space: break
                if j > i and A[j] == A[j-1] or A[j] > val: continue
                num, A[j] = A[j], val + 1
                if num == space:
                    if btrack(0, val, k-1): return True
                if btrack(j + 1, space - num, k): return True
                A[j] = num
            return False
        return btrack(0, val, k)








class Solution1:    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [0] * len(nums)
        def backtrack(i, curSum, k):
            if k == 0:
                return True
            if curSum == target:
                return backtrack(0, 0, k-1)
            for j in range(i, len(nums)):
                if used[j] or curSum + nums[j] > target:
                    continue
                used[j] = 1
                if backtrack(j+1, curSum + nums[j], k):
                    return True
                used[j] = 0
        return backtrack(0, 0, k)
        
        
        
        
        
        
        
        
        
        
        
        
        

class Solution1:    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visited = [0] * len(nums)
        target = sum(nums) / k
        if target != int(target):
            return False
        
        target = int(target)
        nums.sort(reverse=True)
        return self.recur(0, 0, k, target, visited, nums)
    
    def recur(self, i, curSum, k, target, visited, nums):
        if k == 0:
            return True
                
        if curSum == target:
            return self.recur(0, 0, k-1, target, visited, nums)
        
        if i >= len(nums):
            return False
        
        if curSum > target:
            return False
        
        if visited[i] == 0:
            visited[i] = 1
            if self.recur(i + 1, curSum + nums[i], k, target, visited, nums):
                return True
            visited[i] = 0
        
        return self.recur(i+1, curSum, k, target, visited, nums)