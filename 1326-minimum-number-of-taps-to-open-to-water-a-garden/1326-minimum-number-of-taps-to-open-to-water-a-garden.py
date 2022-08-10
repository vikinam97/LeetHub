import collections

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rangeList = []
        for i in range(n+1):
            rangeList.append((i - ranges[i], i + ranges[i]))
        
        rangeList.sort()
        rangeList = collections.deque(rangeList)
        # print(rangeList)
        start = 0
        count = 0
        while start < n:
            end = start
            # print("---", start)
            while rangeList and rangeList[0][0] <= start:
                # print(rangeList[0])
                end = max(end, rangeList.popleft()[1])
            
            if start == end:
                return -1
            
            start = end
            count += 1
        
        return count