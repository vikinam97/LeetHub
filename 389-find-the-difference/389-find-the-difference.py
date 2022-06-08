class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xorS, xorT = 0, 0
        for i in range(len(s)):
            xorS ^= ord(s[i])
            xorT ^= ord(t[i])
            
        xorT = xorT ^ ord(t[len(s)])
        
        return chr(xorS ^ xorT)
            