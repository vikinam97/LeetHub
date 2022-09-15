class Solution:
    
    def recur(self, i, path, string):
        
        if i >= len(string):
            if len(path) == 4:
                self.result.append(".".join(path))
            return
        
        if string[i] == '0':
            path.append('0')
            self.recur(i+1, path, string)
            path.pop()
            return
        
        for j in range(i, len(string)):
            seg = string[i:j+1]
            if int(seg) >= 256:
                return
            path.append(seg)
            self.recur(j+1, path, string)
            path.pop()
        
        return
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        
        self.recur(0, [], s)
        
        return self.result
        
        