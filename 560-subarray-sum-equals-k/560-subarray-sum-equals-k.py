class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = defaultdict(int)
        hashMap[0] = 1
        runningSum = 0
        
        count = 0
        for i in range(len(nums)):
            
            runningSum += nums[i]
            
            if runningSum - k in hashMap:
                count += hashMap[runningSum - k]
            
            hashMap[runningSum] += 1
        
        return count