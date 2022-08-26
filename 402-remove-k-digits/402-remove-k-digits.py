class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Solution - Monotonic Stack
        # Time - O(N)
        # Space - O(N)
        
        stack = []
        count = 0
        for n in num:
            while stack and count < k and int(stack[-1]) > int(n):
                count += 1
                stack.pop()
            
            stack.append(n)
        
        while stack and count < k:
            stack.pop()
            count += 1
            
        if not stack:
            return "0"
        
        return str(int("".join(stack)))
        