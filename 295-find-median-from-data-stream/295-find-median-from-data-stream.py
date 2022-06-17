class MedianFinder:

    def __init__(self):
        import heapq
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)
        if (self.minHeap and self.maxHeap and 
            ((-1 * self.maxHeap[0]) > self.minHeap[0])):
            ele = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * ele)
        
        # uneven sizes
        if len(self.maxHeap) > len(self.minHeap) + 1:
            ele = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * ele)
            
        if len(self.minHeap) > len(self.maxHeap) + 1:
            ele = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * ele)
            

    def findMedian(self) -> float:
        # print(self.maxHeap)
        # print(self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return ((-1 * self.maxHeap[0]) + (self.minHeap[0])) / 2            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()