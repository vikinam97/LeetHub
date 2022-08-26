class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Solution - traversal and make fist !a to a else last to b
        # Time - O(N)
        # Space - O(1)
        
        n = len(palindrome) 
        if n == 1:
            return ""
        palindrome = list(palindrome)
        
        for i in range(n):
            if i == n // 2 and n&1:
                continue
                
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
            
        palindrome[-1] = 'b'
        
        return "".join(palindrome)