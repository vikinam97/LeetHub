class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome) 
        if n == 1:
            return ""
        palindrome = list(palindrome)
        
        for i in range(n):
            if i == n // 2 and n&1:
                continue
                
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                break
            
            if i == n-1:
                palindrome[i] = 'b'
        
        return "".join(palindrome)