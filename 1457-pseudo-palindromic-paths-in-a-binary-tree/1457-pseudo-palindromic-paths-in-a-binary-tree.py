# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.recur(root, 0)
    
    def recur(self, node, path):
        if not node:
            return 0
        
        path = path ^ (1 << node.val)
            
        if not node.left and not node.right:
            count = 1 if (path & path-1) == 0 else 0
        else:
            count = (self.recur(node.left, path) +
               self.recur(node.right, path))
        
        path = path ^ (1 << node.val)
        return count

class Solution1:    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.recur(root, defaultdict(int), 0, 0)
    
    def recur(self, node, freq, even, odd):
        if not node:
            return 0
        
        freq[node.val] += 1
        
        if freq[node.val] & 1:
            even = max(even - 1, 0)
            odd += 1
        else:
            odd = max(odd - 1, 0)
            even += 1
            
        if not node.left and not node.right:
            count = 1 if odd == 0 or odd == 1 else 0
        else:
            count = (self.recur(node.left, freq, even, odd) +
               self.recur(node.right, freq, even, odd))
        
        freq[node.val] = max(0, freq[node.val]-1)
        return count