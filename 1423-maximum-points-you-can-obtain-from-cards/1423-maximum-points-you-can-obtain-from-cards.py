class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        slidingSum = sum(cardPoints[:length - k])
        minSoFar = slidingSum
        j = 0
        for i in range(length - k, length):
            print(slidingSum)
            slidingSum += cardPoints[i]
            slidingSum -= cardPoints[j]
            j += 1
            minSoFar = min(minSoFar, slidingSum)
        
        return sum(cardPoints) -  minSoFar