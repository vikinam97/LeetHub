class Solution:
    
    def recur(self, n, k, path):
        if n <= 0:
            self.result.append(int("".join([ str(c) for c in path])))
            return
        
        for i in range(10):
            if not path and i == 0:
                continue
            
            if path and abs(path[-1] - i) != k:
                continue
            
            path.append(i)
            self.recur(n-1, k, path)
            path.pop()
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.result = []
        
        self.recur(n, k, [])
        
        return self.result