class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ps = [[1]]
        
        for i in range(1, numRows):
            row = [0] * (len(ps[-1]) + 1)
            row[0], row[-1] = 1, 1
            ps.append(row)
            for j in range(1, len(row)-1):
                ps[i][j] = ps[i-1][j] + ps[i-1][j-1]
        
        return ps
            