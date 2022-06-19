class Solution:
    def greatestLetter(self, s: str) -> str:
        # Solution - using hash map bit manipulated
        # Time - O(N)
        # Space - O(1)
        dpLower = 0
        dpUpper = 0
        for i in range(len(s)):
            letter = s[i]
            if ord('a') <= ord(letter) <= ord('z'):
                print('lower', s[i])
                dpLower = dpLower | (1 << (ord(letter) - ord('a')))
            else:
                dpUpper = dpUpper | (1 << (ord(letter) - ord('A')))
        
        i = 26
        while i >= 0:
            if (dpLower & (1 << i)) and (dpUpper & (1 << i)):
                return chr(i + ord('A'))
            i -= 1

        return ''
            
            
        