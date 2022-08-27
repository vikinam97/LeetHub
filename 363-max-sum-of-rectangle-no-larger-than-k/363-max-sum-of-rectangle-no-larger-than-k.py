class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0]) 
        ans = -10**9
        for l in range(C):  # left pointer
            temp, cum = [0]*R, [0]*R
            for r in range(l, C):   # right pointer
                for i in range(R):
                    temp[i]+=matrix[i][r] # compute the sum[]
                    cum[i] = temp[i] + (cum[i-1] if i>0 else 0) # compute the cumulative sum

                bs = []
                for i in range(R):
                    pos = bisect.bisect_left(bs, cum[i]-k)   # find a smallest cum[j] that >=cum[i]-k
                    if cum[i]<=k: 
                        ans = max(ans, cum[i])
                    if pos<len(bs):
                        ans = max(ans, cum[i]-bs[pos])
                        if ans==k: return ans
                    bs.insert(bisect.bisect(bs, cum[i]), cum[i])
        return ans