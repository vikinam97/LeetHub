class DSUF:
    
    def __init__(self, n):
        self.list = [-1] * n
    
    def find(self, a):
        if self.list[a] == -1:
            return a
        self.list[a] = self.find(self.list[a])
        return self.list[a]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if pa == pb:
            return
        
        self.list[pb] = pa

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Solution - disjoint set
        # Time - O(NlogN)
        # Space - O(26) = O(1)
        
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
                
        