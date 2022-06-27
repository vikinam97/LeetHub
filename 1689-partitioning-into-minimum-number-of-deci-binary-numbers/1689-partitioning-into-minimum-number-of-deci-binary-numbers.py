class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(digit) for digit in n)
        # maxSoFar = int(n[0])
        # for num in n:
        #     num = int(num)
        #     maxSoFar = max(maxSoFar, num)
        # return maxSoFar
        