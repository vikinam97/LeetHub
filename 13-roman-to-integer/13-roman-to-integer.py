class Solution:
    def romanToInt(self, s: str) -> int:
        valMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        stack = []
        for i in range(len(s)):
            val = valMap[s[i]]
            if not stack:
                stack.append(val)
            elif stack[-1] >= val:
                stack.append(val)
            else:
                pVal = stack.pop()
                stack.append(val - pVal)
        
        return sum(stack)