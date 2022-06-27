class Solution:
    def minPartitions(self, n: str) -> int:
        maxSoFar = int(n[0])
        for num in n:
            num = int(num)
            maxSoFar = max(maxSoFar, num)
            
        return maxSoFar
        