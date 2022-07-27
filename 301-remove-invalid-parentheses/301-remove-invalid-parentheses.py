class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Solution - backtrack and only include valid backets 
        # Time - O(2^N)
        # Space - O(2^N)
        
        
        leftRem, rightRem = self.getMinRemovals(s)
        self.valids = set()
        
        self.backtrack(0, 0, 0, s, leftRem, rightRem, [])
        
        return self.valids
    def getMinRemovals(self, string):
        l, r = 0, 0
        i = 0
        for i in range(len(string)):
            if string[i] == "(":
                l += 1
            elif string[i] == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return [l, r]
                
    def backtrack(self, i, leftCount, rightCount, string, leftRem, rightRem, path):
        if i >= len(string):
            if leftRem == 0 and rightRem == 0:
                self.valids.add("".join(path))
            return
        
        if string[i] == "(" and leftRem > 0:
            self.backtrack(i+1, leftCount, rightCount, string, leftRem-1, rightRem, path)
        if string[i] == ")" and rightRem > 0:
            self.backtrack(i+1, leftCount, rightCount, string, leftRem, rightRem-1, path)
        
        path.append(string[i])
        
        if string[i] != '(' and string[i] != ')':
            self.backtrack(i+1, leftCount, rightCount, string, leftRem, rightRem, path)
        elif string[i] == '(':
            self.backtrack(i+1, leftCount+1, rightCount, string, leftRem, rightRem, path)
        elif string[i] == ')' and leftCount > rightCount:
            self.backtrack(i+1, leftCount, rightCount+1, string, leftRem, rightRem, path)
        
        path.pop()
        