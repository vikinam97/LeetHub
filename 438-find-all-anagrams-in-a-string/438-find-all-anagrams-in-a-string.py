class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        reqChar, reqCharCount = defaultdict(int), 0
        
        for char in p:
            reqChar[char] += 1
        reqCharCount = len(reqChar.keys())
        
        # print(reqChar, reqCharCount)
        
        seenChar = defaultdict(int)
        seenCharCount = 0
        reqSeenCharCount = 0
        j = 0
        
        result = [] 
        for idx, char in enumerate(s):
            if seenChar[char] == 0:
                seenCharCount += 1
            seenChar[char] += 1
            
            if char in reqChar and reqChar[char] == seenChar[char]:
                reqSeenCharCount += 1
            
            # print(s[j:idx+1])
            while reqSeenCharCount == reqCharCount:
                # print(s[j:idx+1], idx, j, len(p), (idx - j + 1) == len(p), seenCharCount)
                if reqCharCount == seenCharCount and (idx - j + 1) == len(p):
                    # print("found ===> ", j)
                    result.append(j)
                
                seenChar[s[j]] -= 1
                if seenChar[s[j]] == 0:
                    # print("dec -> ", s[j], j)
                    seenCharCount -= 1
                if s[j] in reqChar and seenChar[s[j]] < reqChar[s[j]]:
                    # print('req -> ', s[j], seenChar[s[j]], s[j:idx+1], j)
                    
                    reqSeenCharCount -= 1
                j += 1
                
        return result