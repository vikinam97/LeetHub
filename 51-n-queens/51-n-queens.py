class Solution:
    def createBoard(self, n):
        tempBoard = [];
        for i in range(n):
            tempBoard.append([0] * n)
        return tempBoard;
        
    def solveNQueens(self, n: int) -> List[List[str]]:        
        board = self.createBoard(n);
        
        results = []
        self.traverseQueen(0, board, n, results);
        
        return results;
        
    def traverseQueen(self, q, board, numQueens, results):
        if q == numQueens:
            strBoard = [ "".join(row) for row in board] 
            results.append(strBoard)
            return
            
        for i in range(len(board[0])):
            if board[q][i] != 0:
                continue;
            
            tempBoard = self.placeQueen(board, q, i)
            self.traverseQueen(q+1, tempBoard, numQueens, results);
            
    def placeQueen(self, board, row, col):
        
        a = 'Q'
        b = '.'
        
        tempBoard = [row[:] for row in board]
        
        tempBoard[row][col] = a;
            
        # bottom -> row+1
        i = row+1
        while i < len(board):
            tempBoard[i][col] = b
            i+=1;
            
        # left -> col-1
        i = col-1
        while i >= 0:
            tempBoard[row][i] = b
            i-=1
            
        # right -> col+1
        i = col+1
        while i < len(board[0]):
            tempBoard[row][i] = b
            i+=1
        
        # diagonal left
        i,j = row + 1, col-1
        while i < len(board) and j >= 0:
            tempBoard[i][j] = b
            i+=1;
            j-=1;
        
        # diagonal right
        i,j = row+1, col+1
        while i < len(board) and j < len(board):
            tempBoard[i][j] = b
            i+=1
            j+=1
        
        return tempBoard;