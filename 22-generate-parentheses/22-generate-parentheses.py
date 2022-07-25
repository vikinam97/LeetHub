class Solution:
    def backtrack(self, oc, cc, path):
        if oc == 0 and cc == 0:
            self.validList.append("".join(path))
            return
        
        if oc > 0:
            path.append("(")
            self.backtrack(oc-1, cc, path)
            path.pop()
        
        if cc > oc:
            path.append(")")
            self.backtrack(oc, cc-1, path)
            path.pop()
            
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.validList = []
        self.backtrack(n, n, [])
        return self.validList