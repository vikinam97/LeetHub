class Solution(object):
    def numSubmatrixSumTarget(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        count = 0
        for i in range(cols):
            colsum = [0] * rows
            for j in range(i, cols):
                ht = collections.defaultdict(int)
                rowsum = 0
                ht[0] = 1
                for r in range(rows):
                    colsum[r] += matrix[r][j]
                    rowsum += colsum[r]
                    count += ht[rowsum-k]
                    ht[rowsum] += 1
                    
        return count

# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         prefix = [[0] * len(matrix[0]) for i in range(len(matrix))]
        
#         prefix[0][0] = matrix[0][0]
        
#         for i in range(1, len(matrix)):
#             prefix[i][0] = prefix[i-1][0] + matrix[i][0]
        
#         for j in range(1, len(matrix[0])):
#             prefix[0][j] = prefix[0][j-1] + matrix[0][j]
        
#         for i in range(1, len(matrix)):
#             for j in range(1, len(matrix[0])):
#                 prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
