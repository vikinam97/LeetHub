class Solution:
    def twoEggDrop(self, n: int) -> int:
        l, r = 1, n
        
        def isPossible(x):
            return (x*(x+1)) / 2 >= n
        
        minSoFar = float('inf')
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if isPossible(mid):
                minSoFar = min(minSoFar, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return minSoFar