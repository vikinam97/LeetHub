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
length = len(self.queue)
while length > 1:
self.queue.append(self.queue.pop(0))
length -= 1
result = self.queue.pop(0)
return result
​
def top(self) -> int:
return self.queue[-1]
​
def empty(self) -> bool:
return len(self.queue) == 0
​
```