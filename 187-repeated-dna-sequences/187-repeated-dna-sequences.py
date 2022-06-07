class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subStrHash = {}
        
        for i in range(len(s) - 9):
            subStr = s[i:i+10]
            subStrHash[subStr] = subStrHash.get(subStr, 0) + 1
        
        result = []
        for sstr in subStrHash:
            if subStrHash[sstr] > 1:
                result.append(sstr)
                
        return result