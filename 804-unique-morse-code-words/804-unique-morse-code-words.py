code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashSet = set()
        
        for word in words:
            codeWord = []
            for char in word:
                codeWord.append(code[ord(char) - ord('a')])
            
            codeWord = "".join(codeWord)
            hashSet.add(codeWord)
        
        return len(hashSet)
                