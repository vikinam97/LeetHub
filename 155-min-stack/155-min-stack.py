class MinStack:

    def __init__(self):
        self.minStack = []
        self.minState = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.minState or val < self.minState[-1]:
            self.minState.append(val)
        else:
            self.minState.append(self.minState[-1])

    def pop(self) -> None:
        if self.minStack:
            self.minState.pop()
            return self.minStack.pop()

    def top(self) -> int:
        print(self.minStack)
        print(self.minState)
        if self.minStack:
            return self.minStack[-1]

    def getMin(self) -> int:
        if self.minState:
            return self.minState[-1]
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()