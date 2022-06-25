class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # Solution - using monotonic deque
        # Time - O(N)
        # Space O(N
        
        dequeSum = collections.deque([[0, -1]])
        minSoFar = float('inf')
        slidingSum = 0
        
        for idx in range(len(nums)):
            slidingSum += nums[idx]
            
            while dequeSum and (slidingSum - dequeSum[0][0]) >= k:
                popedEle = dequeSum.popleft()
                minSoFar = min(minSoFar, idx - popedEle[1])
            
            while dequeSum and slidingSum <= dequeSum[-1][0]:
                dequeSum.pop()
            
            dequeSum.append([slidingSum, idx])
        
        return minSoFar if minSoFar != float('inf') else -1
        
        
        
        
        
        
        
        
        
        
