class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maxSoFar = special[0] - bottom
        
        for i in range(1, len(special)):
            a = (special[i-1]+1)
            b = (special[i]-1)
            diff = (b - a) + 1
            maxSoFar = max(maxSoFar, diff)
        
        diffAtTop = top - special[-1] 
        maxSoFar = max(maxSoFar, diffAtTop)
        
        return maxSoFar
    