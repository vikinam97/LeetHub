class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.hashTable = []
        for i in range(10):
            self.hashTable.append([])
        

    def put(self, key: int, value: int) -> None:
        k = key % 10
        # to check value already exist
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i].key == key:
                self.hashTable[k][i].value = value
                return
            
        self.hashTable[k].append(Pair(key, value))

    def get(self, key: int) -> int:
        k = key % 10
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i].key == key:
                return self.hashTable[k][i].value
        return -1

    def remove(self, key: int) -> None:
        k = key % 10
        idx = -1
        for i in range(len(self.hashTable[k])):
            if self.hashTable[k][i].key == key:
                idx = i
                break
        if idx == -1:
            return -1
        
        self.hashTable[k] = self.hashTable[k][:idx] + self.hashTable[k][idx+1:]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)