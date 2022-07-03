class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
	# Base case.
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
		
		# Creat a matrix with all elements as False.
        visited = [[False] * cols for _ in range(rows)]

        ans = []
		# Creat the direction for row and column, the idea is, first we start from left to right, so the row 
		# doesn't move but the columns move +1. Second step, we move from upper to lower, so the 
		# row move by +1, and columns doesn't change. Third step, we move from right to left, so the
		# row doesn't change, but the columns move by -1. Last step, we move from lower to upper, 
		# so the row move by -1, but the columns doesn't change.
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]
		
		# Set up the current row, current column and current state as 0.
        curr_row = curr_col = state = 0
		
		# Write for loop, set the visited place as True, update the next row and next column based on 
		# the directions.
        for _ in range(rows * cols):
            ans.append(matrix[curr_row][curr_col])
            visited[curr_row][curr_col] = True
            next_row = curr_row + drow[state]
            next_col = curr_col + dcol[state]
			
			# if did not reach the upper, lower, left and right boundary and visited is not True, we
			# continue the process to next row and column without any changes.
			# if not, we first update the state by +1 then mod 4, means that we change the direction
			# then we update to next row and next columns.
            if 0 <= next_row < rows and 0 <= next_col < cols and (not visited[next_row][next_col]):
                curr_row, curr_col = next_row, next_col
            else:
                state = (state + 1) % 4
                curr_row, curr_col = curr_row + drow[state], curr_col + dcol[state]

        return ans