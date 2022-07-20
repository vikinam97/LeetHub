class Solution:
    def longestDupSubstring(self, s: str) -> str:
        chrMap = [ord(c) - ord('a') for c in s]
        mod = 2**63 - 1 
        
        def checkSubstr(L):
            cur, k = 0, 1
            for i in range(L):
                cur = (cur + chrMap[L-1-i]*k)%mod
                k = k*26 % mod
            seen = {cur}
            for i in range(L, len(s)):
                cur = (cur * 26 + chrMap[i] - chrMap[i - L] * k) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
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
        