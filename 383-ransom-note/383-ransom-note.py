class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = [0] * 26
        
        for char in magazine:
            hashMap[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            if hashMap[ord(char) - ord('a')] <= 0:
                return False
            hashMap[ord(char) - ord('a')] -= 1
        
        return True
            