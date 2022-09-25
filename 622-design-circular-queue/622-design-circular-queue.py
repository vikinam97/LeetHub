class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = Node('s')
        self.tail = Node('t')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node):
        headNext = self.head.next
        self.head.next = node
        
        node.next = headNext
        node.prev = self.head
        
        headNext.prev = node
    
    def pop(self):
        tailPrev = self.tail.prev
        
        self.tail.prev = tailPrev.prev
        tailPrev.prev.next = self.tail
        
        return tailPrev
        
    def enQueue(self, value: int) -> bool:
        newNode = Node(value)
        if self.size == self.capacity:
            return False
        self.append(newNode)
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        ele = self.pop()
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size <= 0:
            return -1
        
        return self.tail.prev.val
            
    def Rear(self) -> int:
        if self.size <= 0:
            return -1
        return self.head.next.val
        
    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity
        
    
    def debug(self):
        print(self.size)
        t = self.head
        while t:
            print(t.val)
            t = t.next
        print("---------")

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()