```
class Solution:
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
# Solution - DFS
# Time - O(V + E)
# Space - O(V)
self.paths = []
self.dfs(0, len(graph)-1, graph, [], set())
return self.paths
def dfs(self, cur, dest, graph, path, seen):
if cur == dest:
self.paths.append(path[:] + [dest])
if cur in seen:
return
path.append(cur)
seen.add(cur)
for i in graph[cur]:
self.dfs(i, dest, graph, path, seen)
seen.remove(cur)
path.pop()
```