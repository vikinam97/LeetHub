elif edges[i][0] == 1:
aliceEdges.append(edges[i])
else:
bobEdges.append(edges[i])
usedEdgeCount = 0
# connect both edges
for edge in bothEdges:
aReq = aliceSet.union(edge[1]-1, edge[2]-1)
bReq = bobSet.union(edge[1]-1, edge[2]-1)
if aReq and bReq:
usedEdgeCount += 1
# connect individual edges
for edge in aliceEdges:
usedEdgeCount += aliceSet.union(edge[1]-1, edge[2]-1)
for edge in bobEdges:
usedEdgeCount += bobSet.union(edge[1]-1, edge[2]-1)
if aliceSet.countParents() == 1 and bobSet.countParents() == 1:
return len(edges) - usedEdgeCount
return -1
```