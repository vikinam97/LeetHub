class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = {}
        charCount = 0
        maxSoFar = 0
        i, j = 0, 0
        while j < len(s):
            # print(i, j, charCount, j - i + 1, hashSet)
            # to check if it already in sub string
            if hashSet.get(s[j], 0) == 0:
                hashSet[s[j]] = 1
                charCount += 1
            # already in sub string thn remove from begging
            else:
                hashSet[s[j]] += 1
                while charCount != (j - i + 1):
                    hashSet[s[i]] -= 1
                    if hashSet[s[i]] == 0:
                        charCount -= 1
                    i += 1
            maxSoFar = max(maxSoFar, j - i + 1)
            j += 1

                
        return maxSoFar