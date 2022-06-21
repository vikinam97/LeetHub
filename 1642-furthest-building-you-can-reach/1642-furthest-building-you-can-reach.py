class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        heapq.heapify(heap)
        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(heap, -diff)
                else:
                    if ladders == 0:
                        return i - 1
                    else:
                        maximum = -heapq.heappushpop(heap, -diff)
                        bricks += maximum - diff
                        ladders -= 1
        return n - 1