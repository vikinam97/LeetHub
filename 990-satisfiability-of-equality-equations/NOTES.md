dsu = DSUF(26)
def getCharMap(char):
return ord(char) - ord('a')
eqCond, ntEqual = [], []
for eq in equations:
v1, v2 = getCharMap(eq[0]), getCharMap(eq[3])
relation = eq[1]
if relation == '!' :
ntEqual.append([v1, v2])
else:
eqCond.append([v1, v2])
for v1, v2 in eqCond:
dsu.union(v1, v2)
for v1, v2 in ntEqual:
if dsu.find(v1) == dsu.find(v2):
return False
return True
```