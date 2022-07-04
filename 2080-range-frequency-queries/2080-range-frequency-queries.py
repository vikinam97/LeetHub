class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.hashSet = defaultdict(list)
        for i in range(len(arr)):
            self.hashSet[arr[i]].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.hashSet[value], right) - bisect_left(self.hashSet[value], left)