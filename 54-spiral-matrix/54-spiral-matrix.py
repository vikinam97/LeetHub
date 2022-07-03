class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
		
        visited = [[False] * cols for _ in range(rows)]

        ans = []

        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]
		
        curr_row = curr_col = state = 0
		
        for _ in range(rows * cols):
            ans.append(matrix[curr_row][curr_col])
            visited[curr_row][curr_col] = True
            next_row = curr_row + drow[state]
            next_col = curr_col + dcol[state]
            
            if 0 <= next_row < rows and 0 <= next_col < cols and (not visited[next_row][next_col]):
                curr_row, curr_col = next_row, next_col
            else:
                state = (state + 1) % 4
                curr_row, curr_col = curr_row + drow[state], curr_col + dcol[state]

        return ans