class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.hashSet = defaultdict(list)
        for i in range(len(arr)):
            self.hashSet[arr[i]].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.hashSet:
            return 0
        appearenceList = self.hashSet[value]
        l = bisect_left(appearenceList, left)
        r = bisect_right(appearenceList, right)
        
        return r - l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)