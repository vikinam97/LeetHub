class Node:
    def __init__(self, key, val, prev, nxt):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
    
class DLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertLast(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def removeFront(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        else:
            self.head = nxt
            
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        node.next, node.prev = None, None
    
    def print(self):
        temp = self.head
        op = []
        while temp:
            op.append(str(temp.val))
            temp = temp.next 
        print("->".join(op))

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.queue = DLinkedList()
        self.curSize = 0

    def get(self, key: int) -> int:
        # Time - O(1)
        if self.hash.get(key, None) != None:
            node = self.hash[key]
            self.queue.remove(node)
            self.queue.insertLast(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Time - O(1)
        if self.hash.get(key, None) != None:
            node = self.hash[key]
            self.queue.remove(node)
            node.val = value
            self.queue.insertLast(node)
            return
        
        if self.curSize < self.capacity:
            node = Node(key, value, None, None)
            self.queue.insertLast(node)
            self.hash[key] = node
            self.curSize += 1
            return
        
        delNode = self.queue.removeFront();
        self.hash[delNode.key] = None
        node = Node(key, value, None, None) 
        self.queue.insertLast(node)
        self.hash[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)