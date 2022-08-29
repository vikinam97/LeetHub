class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hashMap = defaultdict(list)
        
        stage, dr = 0, 1
        
        for i in range(len(s)):
            hashMap[stage].append(s[i])
            stage = stage + dr
            if stage == numRows - 1 or stage == 0:
                dr = dr * -1
                
        result = []
        
        for key in hashMap:
            result.append("".join(hashMap[key]))
        
        return "".join(result)
        
        