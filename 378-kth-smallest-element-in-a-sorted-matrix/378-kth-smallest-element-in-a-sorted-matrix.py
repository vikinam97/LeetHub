class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heap, -1 * matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return -1 * heap[0]