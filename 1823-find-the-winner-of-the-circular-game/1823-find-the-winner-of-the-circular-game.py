class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def printList(self, list):
        seen = {}
        while list.val not in seen:
            print(list.val)
            seen[list.val] = True
            list = list.next
            
    def findTheWinner(self, n: int, k: int) -> int:
        head = Node("/")
        temp = head
        for i in range(1, n+1):
            temp.next = Node(i)
            temp = temp.next
        temp.next = head.next
        
        prev = temp
        temp = head.next
        head = temp
        
        count = 0
        while count < n:
            self.printList(temp)
            for i in range(1, k):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            print("left -> ", temp.val)
            temp = prev.next
            count += 1
        print(count)
        return temp.val
        
        