# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, x, dep):
        if not node:
            return
        
        if x > self.max:
            temp = {}
            temp[dep] = [node.val]
            self.order.append(temp)
            self.max += 1
        elif x < self.min:
            temp = {}
            temp[dep] = [node.val]
            self.order.appendleft(temp)
            self.min -= 1
        else:
            lvls = self.order[(-1 * self.min) + x]
            if dep not in lvls:
                lvls[dep] = [node.val]
            else:
                lvls[dep].append(node.val)
        
        self.dfs(node.left, x - 1, dep + 1)
        self.dfs(node.right, x + 1, dep + 1)
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = collections.deque([{}])
        self.min = 0
        self.max = 0
        self.dfs(root, 0, 0)
        # print(self.order)
        result = []
        for lvls in self.order:
            # print("-------")
            # print(sorted(lvls.keys()))
            # print("-------")
            temp = []
            for k in sorted(lvls.keys()):
                temp += sorted(lvls[k])
            result.append(temp)

        return result