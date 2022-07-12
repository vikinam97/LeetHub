class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def recur(i, j):
            if j >= len(p):
                return i >= len(s)
            
            if i >= len(s):
                return ((j+1) < len(p) and p[j+1] == '*' and recur(i, j+2))
            
            match = (s[i] == p[j]) or (p[j] == '.')
            if (j+1) < len(p) and p[j+1] == '*':
                return recur(i, j+2) or (match and recur(i+1, j))
            else:
                return (match and recur(i+1, j+1))
                
        return recur(0, 0)