class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = defaultdict(int)
        idMap = {}
        
        for i in range(len(s)):
            idMap[s[i]] = i
            hashMap[s[i]] += 1
        
        for char in hashMap:
            if hashMap[char] == 1:
                return idMap[char]
        
        return -1
        