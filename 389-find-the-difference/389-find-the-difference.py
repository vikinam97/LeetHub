class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xorAll = 0
        for i in range(len(s)):
            xorAll ^= ord(s[i])
            xorAll ^= ord(t[i])
            
        xorAll = xorAll ^ ord(t[len(s)])
        
        return chr(xorAll)
            