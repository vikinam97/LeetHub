class Solution:        
    def calculate(self, s: str) -> int:
        self.pre = { '+': 1, '-': 1, '(' : 1}
        tokenized = self.tokenize(s)
        postfix = self.converPostfix(tokenized)
        return self.evalRPN(postfix)
    
    def converPostfix(self, exprList):
        def checkInt(str):
            if str[0] in ('-', '+'):
                return str[1:].isdigit()
            return str.isdigit()
        
        result = []
        i = 0
        stack = []
        while i < len(exprList):
            token = exprList[i]
            if checkInt(token):
                result.append(token)
            elif token == '(':
                stack.append('(')
            elif token == '-' or token == '+':
                while stack and (stack[-1] != '(' or (self.pre[stack[-1]] < self.pre[token])):
                    result.append(stack.pop())
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            i += 1
        
        return result
    def tokenize(self, s):
        s = s.replace(' ', '')
        s = '(' + s + ')'
        s = s.replace('(-', '(0-')
        
        result = []
        
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                result.append(s[i:j])
                i = j
            elif char == '(' or char == ')' or char == '+' or char == '-':
                result.append(char)
                i += 1
        
        return result
    
    def evalRPN(self, tokens: List[str]) -> int:
        def getPopTwo(stck):
            return [int(stck.pop()), int(stck.pop())]
        
        stack = []
        
        for i  in range(len(tokens)):
            token = tokens[i]
            if token == '+':
                right, left = getPopTwo(stack)
                stack.append(left + right)
            elif token == '-':
                right, left = getPopTwo(stack)
                stack.append(left - right)
            elif token == '*':
                right, left = getPopTwo(stack)
                stack.append(left * right)
            elif token == '/':
                right, left = getPopTwo(stack)
                stack.append(int(left / right))
            else:
                stack.append(token)
                
        return stack[0]