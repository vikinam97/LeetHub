class Solution:
    def checkFeasible(self, capacity, weights, days):
        dayCount = 1
        slidingSum = 0
        for i in range(len(weights)):
            if slidingSum + weights[i] > capacity:
                dayCount += 1
                slidingSum = weights[i]
                if dayCount > days:
                    return False
            else:
                slidingSum += weights[i]
        return True
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        
        minDays = r
        while l <= r:
            mid = (l + r) // 2
            
            if self.checkFeasible(mid, weights, days):
                minDays = min(minDays, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return minDays
                