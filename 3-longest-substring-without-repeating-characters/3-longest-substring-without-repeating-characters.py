class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l=0
        max_length=0
        for r in range(len(s)):
            if s[r] in last_seen:
                l=max(last_seen[s[r]], l)
            
            last_seen[s[r]]=r+1
            max_length=max(max_length, r-l+1)
        return max_length
        
        
        
        # Solution
        # advantage of contigious sub string sliding window
        # Time O(n) traverse array ones
        # Space O(n) max we store all char in set
        # hashSet = {}
        # charCount = 0
        # maxSoFar = 0
        # i, j = 0, 0
        # while j < len(s):
        #     # print(i, j, charCount, j - i + 1, hashSet)
        #     # to check if it already in sub string
        #     if hashSet.get(s[j], 0) == 0:
        #         hashSet[s[j]] = 1
        #         charCount += 1
        #     # already in sub string thn remove from begging
        #     else:
        #         hashSet[s[j]] += 1
        #         while charCount != (j - i + 1):
        #             hashSet[s[i]] -= 1
        #             if hashSet[s[i]] == 0:
        #                 charCount -= 1
        #             i += 1
        #     maxSoFar = max(maxSoFar, j - i + 1)
        #     j += 1
        # return maxSoFar