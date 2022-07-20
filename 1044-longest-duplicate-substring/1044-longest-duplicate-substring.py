class Solution:
    def longestDupSubstring(self, s: str) -> str:
        chrMap = [ord(c) - ord('a') for c in s]
        mod = 2**63 - 1 
        
        def checkSubstr(ln):
            roll, k = 0, 1
            seenMap = {}

            for i in range(ln):
                roll = (roll + chrMap[ln -1 - i] * k) % mod
                k = (k * 26) % mod
            seenMap[roll] = True
            
            for i in range(ln, len(s)):
                delTerm = chrMap[i - ln] * k
                addTerm = chrMap[i]
                roll = (roll * 26 + addTerm - delTerm) % mod
                
                if roll in seenMap:
                    return i - ln + 1
                
                seenMap[roll] = True
            
            return None
        l, r = 0, len(s) - 1
        x, y = 0, 0
        while l <= r:
            mid = l + ((r -l ) // 2)
            dupPos = checkSubstr(mid)
            if(dupPos):
                x, y = dupPos, dupPos + mid 
                l = mid + 1
            else:
                r = mid - 1
        
        return s[x:y]
        