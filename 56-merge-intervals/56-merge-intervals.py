class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def fn(interval):
            return interval[0]
        intervals.sort(key=fn)
        
        result = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(intervals[j][1], end)
                j += 1
            i = j
            result.append([start, end])
        
        return result
            
        