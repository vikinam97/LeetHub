class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        # Solution - monotonic stack
        # Time - O(N)
        # Space - O(N)
        nums.append(-1)
        stack=[-1]
        res=0
        for i in range(len(nums)):
            while nums[i]<nums[stack[-1]]:
                idx=stack.pop()
                res+=nums[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return res%(10**9+7)