class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        chrMap = defaultdict(list)
        
        for i, char in enumerate(s):
            chrMap[char].append(i)
        
        sm = 0
        for char in chrMap:
            for i, idx in enumerate(chrMap[char]):
                leftSubs = 1
                rightSubs = 1
                chrLen = len(chrMap[char]) - 1
                if i == 0:
                    leftSubs = idx + 1
                else:
                    leftSubs = idx - chrMap[char][i-1]
                
                if i == (chrLen):
                    rightSubs = (len(s)) - idx
                else: 
                    rightSubs = chrMap[char][i+1] - idx
                
                sm += leftSubs * rightSubs
                    
                    
        print(chrMap)
        return sm