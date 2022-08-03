def bfs(self, varA, varB, graph):
childs = [(varA, 1)]
seenSet = {}
while childs:
nxt = []
for edge in childs:
var, val = edge
if var == varB:
return val
if var in seenSet:
continue
seenSet[var] = 1
for nVar, nVal in graph[var]:
nxt.append((nVar, nVal * val))
childs = nxt
return -1
```