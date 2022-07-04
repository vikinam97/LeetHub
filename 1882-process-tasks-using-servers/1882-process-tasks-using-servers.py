class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(idle)
        
        busy = []
        
        res = []
        curr_time = 0
        
        for t, task in enumerate(tasks):
            curr_time = max(curr_time, t)
            
            while busy and busy[0][0] <= curr_time:
                done_time, weight, idx = heapq.heappop(busy)
                curr_time = done_time
                heapq.heappush(idle, (weight, idx))
            
            if not idle:
                done_time, weight, idx = heapq.heappop(busy)
                curr_time = done_time
                heapq.heappush(idle, (weight, idx))
            
            # if idle:
            weight, idx = heapq.heappop(idle)
            res.append(idx)
            heapq.heappush(busy, (curr_time + task, weight, idx))
                
        return res