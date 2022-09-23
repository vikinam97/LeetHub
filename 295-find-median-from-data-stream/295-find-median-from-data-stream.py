from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -1*num)
        
        if self.minHeap and self.maxHeap and (-1*self.maxHeap[0]) > self.minHeap[0]:
            num = heappop(self.maxHeap)
            heappush(self.minHeap, -1*num)
        
        self.balance()
        
    def balance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            num = -1*heappop(self.maxHeap)
            heappush(self.minHeap, num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            num = heappop(self.minHeap)
            heappush(self.maxHeap, -1*num)
        

    def findMedian(self) -> float:
        
        if len(self.minHeap) < len(self.maxHeap):
            return -1*self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + (-1*self.maxHeap[0])) / 2
        
            
        
        
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()