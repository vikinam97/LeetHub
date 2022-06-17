class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # Solution - using monotonic deque
        # Time - O(N)
        # Space O(N)
        
        slidingSum = 0
        minSoFar = float('Inf')
        
        monoq = collections.deque([(0, -1)])
        
        for i in range(len(nums)):
            
            slidingSum += nums[i]
            
            if nums[i] > 0:
                while monoq and (slidingSum - monoq[0][0]) >= k:
                    popped = monoq.popleft()
                    minSoFar = min(minSoFar, i - popped[1])
            
            while monoq and slidingSum <= monoq[-1][0]:
                monoq.pop()
            
            monoq.append((slidingSum, i))
        
        return minSoFar if minSoFar != float('Inf') else -1
        
        
        
        
        
        
        
        
        
        
