class MyCalendar:
    # Solution - using BST of intervals
    # Time - O(NlogN) worst O(N^2) 
    # Space - O(N)
    
    def __init__(self):
        self.bookings = None

    def book(self, start: int, end: int) -> bool:
        if self.bookings == None:
            self.bookings = BSTNode(start, end)
            return True
        
        return self.bookings.checkInsert(start, end)

class BSTNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
    def checkInsert(self, start, end):
        if not self:
            return 
        
        if self.start <= start < self.end:
            return False
        
        if start >= self.end:
            if self.right:
                return self.right.checkInsert(start, end)
            
            self.right = BSTNode(start, end)
            return True
        
        elif end <= self.start:
            if self.left:
                return self.left.checkInsert(start, end)
            
            self.left = BSTNode(start, end)
            return True