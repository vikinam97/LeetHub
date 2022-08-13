# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
#         days = [0] * ((10**5)+1)
        
#         events.sort(key = lambda x: (-1*x[0], x[1]))
        
#         count = 0
        
#         for s, e in events:
#             for day in reversed(range(s, e+1)):
#                 if days[day] == 0:
#                     days[day] = 1
#                     count += 1
#                     break
        
#         return count
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        n = max(events, key=lambda x: x[1])[1]
        
        cnt = 0
        i = 0
        for day in range(1, n+1):
            while i < len(events) and events[i][0] == day:
                heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heappop(heap)

            if heap:
                curr = heappop(heap)
                cnt += 1

        return cnt