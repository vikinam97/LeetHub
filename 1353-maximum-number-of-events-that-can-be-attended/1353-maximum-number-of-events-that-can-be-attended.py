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
        n = len(events)
        # edge case: only 1 event available
        if n == 1:
            return 1

        # sort all events w.r.t. their starting days
        events.sort()

        # "attend_day" is the actual day we are at now, which is initialized
        # by the start day of the earliest event
        attend_day = events[0][0]

        # this is a critical variable, indicating currently the earliest event that
        # we have not checked yet (initialized by index 0 as of the earliest event)
        event_to_consider = 0

        # the min-heap to store other ongoing events while at the day = "attend_day"
        ongoing_events = []

        # the final maximum number of events to attend
        res = 0

        # the iteration process continues if there is still ongoing event,
        # or we have not considered all the given events
        while ongoing_events or event_to_consider < n:
            if not ongoing_events:
                # we do not know what are ongoing events at the day = "attend_day",
                # so we need to reset the attend_day = events[event_to_consider][0]
                attend_day = events[event_to_consider][0]
            else:
                # among the ongoing events, we pick the one that ends the earliest, i.e.,
                # the smallest end day, and increment "attend_day" by 1 (the next day)
                heapq.heappop(ongoing_events)
                attend_day += 1
                res += 1

            # we check the events that have not been considered to see
            # how many of them would start at the at the new "attend_day"
            while event_to_consider < n:
                if events[event_to_consider][0] == attend_day:
                    # for each ongoing event, store its end day
                    heapq.heappush(ongoing_events, events[event_to_consider][1])
                    event_to_consider += 1
                else:
                    # no more event starts at day = "attend_day"
                    break

            # ignore those past-due previous events
            while ongoing_events and ongoing_events[0] < attend_day:
                heapq.heappop(ongoing_events)

        return res