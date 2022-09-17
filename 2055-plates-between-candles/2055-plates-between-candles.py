class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        starSum, barIdxs = [0]*len(s), []
        
        for i in range(len(s)):
            if s[i] == '|':
                barIdxs.append(i)
                starSum[i] = starSum[i-1]
            else:
                starSum[i] = starSum[i-1] + 1
            
        result = []
        # print(barIdxs)        
        # print(starSum)

        for s, e in queries:
            sb = bisect.bisect_left(barIdxs, s)
            eb = bisect.bisect_right(barIdxs, e)
            # print(sb, eb)
            
            if sb == eb:
                result.append(0)
                continue
            
            startStarSum = starSum[barIdxs[sb]]
            lastStarSum = starSum[barIdxs[eb-1]]

            # print(startStarSum, lastStarSum)
            # print("-----------")
            
            result.append(lastStarSum - startStarSum)
            
        return result
            
        