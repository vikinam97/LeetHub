# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses.sort(key=lambda c: c[1])
#         A, curr = [], 0
#         for dur, ld in courses:
#             heapq.heappush(A,-dur)
#             curr += dur
#             if curr > ld: curr += heapq.heappop(A)
#         return len(A)

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        
        courses.sort(key=lambda x:x[1])
        # print(courses)
        curTotalTime = 0
        maxSoFar = 0
        for idx in range(len(courses)):
            duration, lastDay = courses[idx]
            
            curTotalTime += (duration)
            heapq.heappush(heap, -1 * duration)
            
            if curTotalTime > lastDay:
                curTotalTime +=  heapq.heappop(heap)
            

            # print(curTotalTime, heap)
            maxSoFar = max(maxSoFar, len(heap))
        
        return maxSoFar
        