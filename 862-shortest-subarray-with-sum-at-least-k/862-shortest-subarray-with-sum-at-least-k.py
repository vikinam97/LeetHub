class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        d = collections.deque([(-1,0)])
        sums = 0
        res = len(nums) + 1

        for i,n in enumerate(nums):
            sums += n
            if n > 0:
                while d and sums-d[0][1] >= k:
                    res = min(res,i-d.popleft()[0])        
            else:
                while d and sums <= d[-1][1]:
                    d.pop()
            d.append((i,sums))
        if res == len(nums)+1:
            return -1
        else:
            return res
        
        
#         slidingSum = 0
#         minSoFar = float('Inf')
        
#         monoq = collections.deque()
        
#         for i in range(len(nums)):
#             slidingSum += nums[i]
#             minSoFar = min(minSoFar, i+1)
            
#             # sum, index
#             lastPop = [float('Inf'), float('Inf')]
            
#             # minimize the window
#             while monoq and (slidingSum - monoq[0][0]) >= k:
#                 lastPop = monoq.popLeft()
                
#             if lastPop[0] != float('Inf'):
#                 minSoFar = min(minSoFar, i - lastPop[1])
                
#             while monoq and monoq[0][0] < slidingSum:
#                 monoq.popleft()
            
#             monoq.append([slidingSum, i])
        
        
#         return minSoFar
        
        
        
        
        
        
        
        
        
        
