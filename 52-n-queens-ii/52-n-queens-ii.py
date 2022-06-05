class Solution:
    def totalNQueens(self, n: int) -> int:
        colSet = {}
        posSet = {}
        negSet = {}
        
        def setQueen(row, col, tpe):
            place = 1 if tpe == 'place' else None
            
            colSet[col] = place
            posSet[row-col] = place
            negSet[row+col] = place
        
        def traverseQueen(q):
            if q == n:
                return 1
            sum = 0
            for i in range(n):
                if colSet.get(i) or posSet.get(q-i) or negSet.get(q+i):
                    continue;
                    
                setQueen(q, i, 'place')
                sum += traverseQueen(q+1)
                setQueen(q, i, 'remove')
                
            return sum
        
        return traverseQueen(0)