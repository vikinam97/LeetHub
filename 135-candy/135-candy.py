class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [0] * len(ratings)
        right = [0] * len(ratings)
        left[0] = 1
        right[-1] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] += right[i+1] + 1
            else:
                right[i] = 1
        
        total = 0
        for i in range(len(ratings)):
            total += max(left[i], right[i])
        
        return total