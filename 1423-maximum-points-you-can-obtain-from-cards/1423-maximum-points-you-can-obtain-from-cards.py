class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Solution - min sum sub array 
        # Time - O(N)
        # Space - O(1)
        length = len(cardPoints)
        slidingSum = sum(cardPoints[:length - k])
        minSoFar = slidingSum
        j = 0
        for i in range(length - k, length):
            slidingSum += cardPoints[i]
            slidingSum -= cardPoints[j]
            j += 1
            minSoFar = min(minSoFar, slidingSum)
        
        return sum(cardPoints) -  minSoFar