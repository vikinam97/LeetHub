class Solution:
    def countBits(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & n-1
        return count
    
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        countBucket = [0] * 32
        
        for i in range(len(nums)):
            countBucket[self.countBits(nums[i])] += 1
            
        result = 0
        for i in range(32):
            for j in range(32):
                if i + j >= k:
                    result += countBucket[i] * countBucket[j]
        
        return result
        
        
        
        
        
        
        
        

class Solution1:
    def countBits(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & n-1
        return count
    
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Solution - bit logic
        # Time - O(NlogN)
        # Space - O(N)
        
        nums = list(set(nums))
        count = 0
        
        for i in range(len(nums)):
            nums[i] = self.countBits(nums[i])
    
        nums.sort()
        
        for i in range(len(nums)):
            bitCount = nums[i]
            idx = bisect_left(nums, k - bitCount)
            count += len(nums) - idx
                
        return count