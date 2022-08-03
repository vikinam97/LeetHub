class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
    def checkInsert(self, start, end):
        # print(self.start, self.end)
        if not self:
            return 
        
        if self.start <= start < self.end:
            return False
        
        if start >= self.end:
            if self.right:
                return self.right.checkInsert(start, end)
            
            self.right = Node(start, end)
            return True
        
        elif end <= self.start:
            if self.left:
                return self.left.checkInsert(start, end)
            
            self.left = Node(start, end)
            return True
            

class MyCalendar:
    def __init__(self):
        self.bookings = None

    def book(self, start: int, end: int) -> bool:
        # print("-----------")
        # print(start, end)
        # print("-")
        if self.bookings == None:
            self.bookings = Node(start, end)
            return True
        
        return self.bookings.checkInsert(start, end)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)