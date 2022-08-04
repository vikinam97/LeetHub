# function return true if the tree is complete else false

class Solution():
    def isCompleteBT(self, root):
        bfs = [root]
        
        foundNone = False
        
        while bfs:
            nxt = []
            for node in bfs:
                if node == None:
                    foundNone = True
                    continue
                
                if foundNone:
                    return False
                    
                nxt.append(node.left)
                nxt.append(node.right)
            
            bfs = nxt
        
        return True
        



#{ 
 # Driver Code Starts
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=='__main__':
    
    root = None
    t = int(input())
    for i in range(t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        if(obj.isCompleteBT(root)):
            print("Complete Binary Tree")
        else:
            print("Not Complete Binary Tree")
# } Driver Code Ends