class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = defaultdict(int)
        for i in range(len(t)):
            sMap[t[i]] += 1
        
        for i in range(len(s)):
            if sMap[s[i]] <= 0:
                return False
            sMap[s[i]] -= 1
            
        return True