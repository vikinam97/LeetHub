class Solution:
    
    def solve(self, x, board, fillList, rowSet, colSet, subSet):

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
        # Solution - hash + backtracking
        # Time - O(9 ^ (9*9))
        # Space - O(9*9)
        
        rowSet, colSet, subSet = [0] * 9, [0] * 9, defaultdict(set)
        
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

                
        