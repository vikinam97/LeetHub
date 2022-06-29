class MyHashSet:

    def __init__(self):
        # Time O(1)
        self.hashTable = []
        for i in range(10):
            self.hashTable.append([])

    def add(self, key: int) -> None:
        k = key % 10
        # to check value already exist
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i] == key:
                return
            
        self.hashTable[k].append(key)

    def remove(self, key: int) -> None:
        k = key % 10
        idx = -1
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i]== key:
                idx = i
                break
                
        if idx == -1:
            return -1
        
        self.hashTable[k] = self.hashTable[k][:idx] + self.hashTable[k][idx+1:]
        

    def contains(self, key: int) -> bool:
        k = key % 10
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i]== key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)