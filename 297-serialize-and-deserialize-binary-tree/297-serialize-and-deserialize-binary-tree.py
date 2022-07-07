# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        def dfs(node, result):
            if not node:
                result.append('-')
                return
            
            result.append(str(node.val))
            dfs(node.left, result)
            dfs(node.right, result)
            
        resList = []
        dfs(root, resList)
        return "#".join(resList)

    def deserialize(self, data):
        self.cur = 0
        def dfs(nodeList):
            if nodeList[self.cur] == '-':
                return None
            
            node = TreeNode(int(nodeList[self.cur]))
            self.cur += 1
            node.left = dfs(nodeList)
            self.cur += 1
            node.right = dfs(nodeList)
            
            return node
            
        return dfs(data.split('#'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))