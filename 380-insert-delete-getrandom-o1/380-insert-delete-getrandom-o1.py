class RandomizedSet:

    def __init__(self):
        self.hashMap = set()
        self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap.add(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            self.hashMap.remove(val)
            return True
        return False
    
    def getRandom(self) -> int:
        keys = list(self.hashMap)
        # self.count += 1
        # return keys[self.count % len(keys)]
        return random.choice(keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()