class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hMax = 0
        for i in range(1, len(horizontalCuts)):
            hMax = max(hMax, horizontalCuts[i] - horizontalCuts[i-1]);
            
        vMax = 0
        for i in range(1, len(verticalCuts)):
            vMax = max(vMax, verticalCuts[i] - verticalCuts[i-1]);
            
        return (hMax * vMax) % ((10 ** 9) + 7)