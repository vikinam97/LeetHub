

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        
        courses.sort(key=lambda x:x[1])
        curTotalTime = 0
        
        for idx in range(len(courses)):
            duration, lastDay = courses[idx]
            
            curTotalTime += (duration)
            heapq.heappush(heap, -1 * duration)
            
            if curTotalTime > lastDay:
                curTotalTime +=  heapq.heappop(heap)

        return len(heap)
        