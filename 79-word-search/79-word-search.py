class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.diList = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = [[0] * len(board[0]) for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(i, j, 0, board, visited, word):
                    return True
        
        return False
    
    def backtrack(self, i, j, wi, board, visited, word):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] != 0:
            return wi >= len(word) 
        
        if wi >= len(word):
            return True
        
        if board[i][j] != word[wi]:
            return False
        
        visited[i][j] = 1
        for di, dj in self.diList:
            x, y = i + di, j + dj
            
            if self.backtrack(x, y, wi + 1, board, visited, word):
                return True
        
        visited[i][j] = 0
        return False
        