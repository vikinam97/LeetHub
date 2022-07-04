class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(idle)
        
        # done_time, weight, idx
        busy = []
        
        res = []
        curr_time = 0
        
        for t, task in enumerate(tasks):
            # if curr_time is less than t then curr_time = t because time has advanced when getting the next task
            # else if curr_time is greater than t then we "wait" till curr_time
            curr_time = max(curr_time, t)
            
            # drain busy heap for all tasks that are done before curr_time
            while busy and busy[0][0] <= curr_time:
                done_time, weight, idx = heapq.heappop(busy)
                curr_time = done_time
                heapq.heappush(idle, (weight, idx))
                
            # if there are no servers idle, pull one from busy and jump time
            if not idle:
                done_time, weight, idx = heapq.heappop(busy)
                curr_time = done_time
                heapq.heappush(idle, (weight, idx))
            
            # at this point we have an available server for current task
            weight, idx = heapq.heappop(idle)
            res.append(idx)
            # push done_time to busy heap
            heapq.heappush(busy, (curr_time + task, weight, idx))
        
        return res