```
class MyStack:
​
def __init__(self):
self.queue = []
​
def push(self, x: int) -> None:
self.queue.append(x)
​
def pop(self) -> int:
tempQueue = []
while len(self.queue) > 1:
tempQueue.append(self.queue.pop(0))
result = self.queue.pop()
while tempQueue:
self.queue.append(tempQueue.pop(0))
return result
​
def top(self) -> int:
return self.queue[-1]
​
def empty(self) -> bool:
return len(self.queue) == 0
```