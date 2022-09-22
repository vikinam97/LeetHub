class Solution:
    def reverseWords(self, s: str) -> str:
        
        wordList = s.split(" ")
        
        wordList = [ word[::-1] for word in wordList]
        
        
        return " ".join(wordList)
        
        