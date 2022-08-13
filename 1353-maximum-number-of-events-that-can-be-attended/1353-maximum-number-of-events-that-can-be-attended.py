class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Solution - attend event with recent end from current day
        # Time - O(NlogN)
        # Space - O(N)
        
        events.sort()
        heap = []
        lastDay = max(events, key=lambda x: x[1])[1]
        
        i = 0
        attended = 0
        for curDay in range(1, lastDay + 1):
            
            while i < len(events) and events[i][0] == curDay:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            while heap and heap[0] < curDay:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                attended += 1
        
        return attended

class Solution1:
    # TLE - attend event on last possible date of event
    # Time - O(NlogN) + O(N*(S-E))
    #     - N - no of events
    #     - E - end of event
    #     - S - start of event
    # Space - O(N)
    
    def maxEvents(self, events: List[List[int]]) -> int:
        days = [0] * ((10**5)+1)
        
        events.sort(key = lambda x: (-1*x[0], x[1]))
        
        count = 0
        
        for s, e in events:
            for day in reversed(range(s, e+1)):
                if days[day] == 0:
                    days[day] = 1
                    count += 1
                    break
        
        return count

            
            
