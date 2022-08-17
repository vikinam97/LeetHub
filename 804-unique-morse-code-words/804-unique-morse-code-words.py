code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Solution - hash set
        # Time - O(N*M)
        #     - N = no of words
        #     - M = len of word
        # Space - O(N*M)
        
        hashSet = set()
        
        for word in words:
            codeWord = []
            for char in word:
                codeWord.append(code[ord(char) - ord('a')])
            codeWord = "".join(codeWord)
            hashSet.add(codeWord)
        
        return len(hashSet)
                