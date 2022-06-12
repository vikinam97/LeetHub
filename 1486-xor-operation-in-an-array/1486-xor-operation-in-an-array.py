class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        runSum = 0
        for i in range(n):
            runSum ^= start + 2 * i
        return runSum
            