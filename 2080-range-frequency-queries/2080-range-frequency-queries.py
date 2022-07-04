class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.map = defaultdict(list)
        for i in range(len(arr)):
            self.map[arr[i]].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.map:
            return 0
        else:
            leftIndex = -1
            rightIndex = -1
            start = 0
            indices = self.map[value]
            end = len(indices)-1
            while start <= end:
                mid = start + (end - start)//2
                if indices[mid] >= left:
                    leftIndex = mid
                    end = mid - 1
                else:
                    start = mid + 1
            start = 0
            end = len(indices)-1
            
            while start <= end:
                mid = start + (end - start)//2
                if indices[mid] <= right:
                    rightIndex = mid
                    start = mid + 1
                else:
                    end = mid - 1
            if rightIndex != -1 and leftIndex != -1:
                return rightIndex - leftIndex + 1
            else:
                return 0


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)