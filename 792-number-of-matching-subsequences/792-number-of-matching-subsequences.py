class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Solution - hash map and carving of word from first
        # Time - O(S + W * 50 + S * W)
        #     S = len of s
        #     W = len of words
        # Space - O(S * W * 50)
        
        def reverseToList(word):
            result = [""] * len(word)
            for idx, char in enumerate(word):
                result[(len(word)-1) - idx] = char
            return result
            
        hashMap = {}
        for char in s:
            hashMap[char] = []
        
        for word in words:
            temp = reverseToList(word)
            if temp[-1] in hashMap:
                hashMap[temp[-1]].append(temp)
                
        count = 0
        for char in s:
            aWords = hashMap[char]
            hashMap[char] = []
            
            for aWord in aWords:
                aWord.pop()
                if len(aWord) == 0:
                    count += 1
                    continue
                if aWord[-1] in hashMap:
                    hashMap[aWord[-1]].append(aWord)
        
        return count