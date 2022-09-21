class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x: (x[0], x[1]))
        
        result = []
        
        i = 0
        
        while i < len(intervals):
            start, end = intervals[i]
            j = i+1
            while j < len(intervals) and end >= intervals[j][0]:
                end = max(end, intervals[j][1])
                j += 1
            
            result.append([start, end])
            i = j        
        
        return result
        