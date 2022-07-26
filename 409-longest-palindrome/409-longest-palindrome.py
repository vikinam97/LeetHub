class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Solution - hash map
        # Time - O(N)
        # Space - O(N)
        
        hashMap = defaultdict(int)
        for i in range(len(s)):
            hashMap[s[i]] += 1
            
        totalCount, oddCount = 0, 0
        for key in hashMap:
            count = hashMap[key]
            if count & 1:
                totalCount += (count - 1)
                oddCount += 1
            else:
                totalCount += count
        
        return totalCount if oddCount == 0 else totalCount + 1 
                
        
        