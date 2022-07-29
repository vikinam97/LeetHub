MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def toInt(node):
    num = 0
    while node:
        num = (num * 10) + node.data
        node = node.next
    return num
    
def multiplyTwoList(head1, head2):
    a = toInt(head1)
    b = toInt(head2)
    return (a % MOD * b % MOD) % MOD