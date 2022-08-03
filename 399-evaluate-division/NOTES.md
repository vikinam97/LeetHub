```
class Solution:
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
# Solution - BFS
# Time - O(Q*N)
#     - N -> no of variables
#     - Q -> no of queries
# Space - O(N)
graph = {}
varSet = set()
for i in range(len(equations)):
varA, varB = equations[i]
val = values[i]
varSet.add(varA)
varSet.add(varB)
if varA not in graph:
graph[varA] = []
graph[varA].append((varB, val))
if varB not in graph:
graph[varB] = []
graph[varB].append((varA, 1 / val))
result = []
for i in range(len(queries)):
varA, varB = queries[i]