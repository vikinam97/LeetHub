if not tNode:
return False
if not lNode:
return True
if tNode.val != lNode.val:
return False
return self.checkcontinuous(tNode.left, lNode.next) or self.checkcontinuous(tNode.right, lNode.next)
def dfs(self, tNode, lNode):
if not tNode and not lNode:
return True
if not tNode:
return False
if not lNode:
return True
if tNode.val == lNode.val and self.checkcontinuous(tNode, lNode):
return True
return self.dfs(tNode.left, lNode) or self.dfs(tNode.right, lNode)
```