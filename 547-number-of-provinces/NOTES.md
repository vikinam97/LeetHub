```
class DSUF:
def __init__(self, n):
self.arr = [-1] * n
def find(self, node):
if self.arr[node] == -1:
return node
self.arr[node] = self.find(self.arr[node])
return self.arr[node]
def union(self, a, b):
aP = self.find(a)
bP = self.find(b)
if aP == bP:
return
self.arr[aP] = bP
def countParent(self):
count = 0
for i in self.arr:
if i == -1:
count += 1
return count
​
class Solution:
def findCircleNum(self, isConnected: List[List[int]]) -> int:
# Solution - Disjoint set + path compression
# Time - O(ElogV)
# Space - O(V)
V = len(isConnected)
dSet = DSUF(V)
for i in range(V):