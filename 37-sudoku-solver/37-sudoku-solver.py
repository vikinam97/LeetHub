class Solution:
    
    def solve(self, x, board, fillList, rowSet, colSet, subSet):
        # print(x, board)
        if x >= len(fillList):
            return True
        
        i, j = fillList[x]      
        
        for p in range(1, 9+1):
            key = str(p)
            if (key in rowSet[i] or 
                key in colSet[j] or 
                key in subSet[(i // 3, j // 3)]):
                continue

            rowSet[i].add(key)
            colSet[j].add(key)
            subSet[(i // 3, j // 3)].add(key)
            board[i][j] = str(p)

            if self.solve( x + 1, board, fillList, rowSet, colSet, subSet):
                return True

            board[i][j] = '.'
            rowSet[i].remove(key)
            colSet[j].remove(key)
            subSet[(i // 3, j // 3)].remove(key)
                        
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        rowSet, colSet, subSet = [0] * 9, [0] * 9, {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 1): set(),
            (2, 0): set(),
            (2, 1): set(),
            (2, 2): set(),
        }
        
        fillList = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    fillList.append((i, j))
                    continue
                    
                if rowSet[i] == 0:
                    rowSet[i] = set()
                rowSet[i].add(board[i][j])
                
                if colSet[j] == 0:
                    colSet[j] = set()
                colSet[j].add(board[i][j])
                
                if (i // 3, j // 3) not in subSet:
                    subSet[(i // 3, j // 3)] = set()
                subSet[(i // 3, j // 3)].add(board[i][j])
                
        self.solve(0, board, fillList, rowSet, colSet, subSet)

                
        