class Solution:
    def concatenatedBinary(self, n: int) -> int:
        places_shifted = 0        
        ans = 0

        for num in range(1, n+1):
            # places_shifted is the number of bits
            if num & (num-1) == 0: places_shifted += 1
            # ans will be shifted by places_shifted and num will be added
            ans = ((ans << places_shifted) + num) % (10**9 + 7)

        return ans