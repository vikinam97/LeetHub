class Solution:
    def countBits(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & n-1
        return count
    
    def binarySearch(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
                
        return l
    
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        count = 0
        
        for i in range(len(nums)):
            nums[i] = self.countBits(nums[i])
    
        nums.sort()
        
        for i in range(len(nums)):
            bitCount = nums[i]
            idx = bisect_left(nums, k - bitCount)
            if idx >= 0:
                count += len(nums) - idx
                
        return count