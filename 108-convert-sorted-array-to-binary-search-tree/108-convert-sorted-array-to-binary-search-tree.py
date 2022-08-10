# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, nums):
        if not nums: 
            return None
        
        mid = 0 + ((len(nums) - 1) // 2)
        
        node = TreeNode(nums[mid])
        
        node.left = self.recur(nums[:mid])
        node.right = self.recur(nums[mid+1:])
        
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Solution - greedy
        # Time - O(N)
        # Space - O(logN)
        
        return self.recur(nums)
        
        