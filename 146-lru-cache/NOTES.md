self.queue.insertLast(node)
return node.val
else:
return -1
​
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
```