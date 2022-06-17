class MedianFinder:

    def __init__(self):
        self.small_heap = []  # Max Heap
        self.big_heap = []  # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -1 * num)

        if self.small_heap and self.big_heap and (-1 * self.small_heap[0]) > self.big_heap[0]:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, val)

        if len(self.small_heap) > len(self.big_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, val)
        if len(self.big_heap) > len(self.small_heap) + 1:
            val = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap, -1 * val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.big_heap):
            return -1 * self.small_heap[0]
        if len(self.big_heap) > len(self.small_heap):
            return self.big_heap[0]

        return (self.big_heap[0] + (-1 * self.small_heap[0])) / 2          


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()