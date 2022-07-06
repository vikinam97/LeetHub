# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def dfs(self, start, end):
        if start > end: return [None]
        if start == end: return [TreeNode(start)]
        
        result = []
        for i in range(start, end+1):
            leftTrees = self.dfs(start, i-1)
            rightTrees = self.dfs(i+1, end)

            for l in leftTrees:
                for r in rightTrees:
                    head = TreeNode(i)
                    head.left = l
                    head.right = r
                    result.append(head)
        return result
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(1, n)
    
    