class Solution:
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
                