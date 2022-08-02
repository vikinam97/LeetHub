class Solution:
    # your task is to complete this function
    # function should delete all the Nodes greater than or equal to k
    # function should return the new head to pointer
    def deleteNode(self, root, k):
        if not root:
            return root
        
        if root.data >= k:
            return self.deleteNode(root.left, k)
        
        root.right = self.deleteNode(root.right, k)
        
        return root