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
            # sb = bisect.bisect_left(barIdxs, s)
            # eb = bisect.bisect_right(barIdxs, e)
            
            l = bisect.bisect_left(barIdxs, s)
            
            # find the right most candles in the query
            r = bisect.bisect_right(barIdxs, e)
            
            # if l == r, it means there is no candle in
            # the query range
            if l == r:
                result.append(0)
                continue
            
            # find the left most candle index in original array
            l_idx = barIdxs[l]
            
            # find the right most candle index in original array
            r_idx = barIdxs[r-1]
            
            # find the candles count by checking the index in cand_idx
            cand_count = r - l
            
            # `r_idx - l_idx + 1`: the number of something between
            # left most and right most candles
            # then minus the number of candles count
            result.append(r_idx - l_idx + 1 - cand_count)
            
        return result
            
        