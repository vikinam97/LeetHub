class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [float('inf')] * len(triangle)
        
        curr = [float('inf')] * len(triangle)
        
        prev[0] = triangle[0][0]
        
        for row in range(0, len(triangle)-1):
            for col in range(len(triangle[row])):
                num = triangle[row+1][col]
                num2 = triangle[row+1][col+1]
                curr[col] = min(curr[col], num + prev[col])
                curr[col+1] = min(curr[col+1], num2 + prev[col])
            
            prev = curr
            curr = [float("inf")] * len(triangle)
        
        minSum = float("inf")
        for i in range(len(prev)):
            minSum = min(minSum, prev[i])
        
        return minSum
        
        