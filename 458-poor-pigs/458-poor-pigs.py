class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        c = 0
        while pow(minutesToTest/minutesToDie+1,c)<buckets:
            c += 1
        return c
        