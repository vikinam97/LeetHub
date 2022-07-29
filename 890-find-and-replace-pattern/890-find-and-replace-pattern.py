class Solution:
    
    def colorCode(self, word):
        hashMap = {}
        count = 0
        code = []
        for i in range(len(word)):
            if word[i] not in hashMap:
                count += 1
                hashMap[word[i]] = count
            code.append(str(hashMap[word[i]]))
        return "#".join(code)
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Solution - color code
        # Time - O(N*M)
        #      - N = no of words
        #      - M = length of word
        # Space - O(M)
        
        patternCode = self.colorCode(pattern)
        
        result = []
        
        for i in range(len(words)):
            if patternCode == self.colorCode(words[i]):
                result.append(words[i])
        
        return result