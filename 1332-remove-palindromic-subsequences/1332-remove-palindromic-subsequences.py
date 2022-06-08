class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def checkPlaindrome(string):
            i, j = 0, len(string) -1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1 
            return True
        
        if checkPlaindrome(s):
            return 1
        
        return 2