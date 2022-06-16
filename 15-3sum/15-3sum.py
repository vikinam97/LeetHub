class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [];
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            if a == nums[i-1] and i != 0:
                continue
            
            j, k = i+1, len(nums)-1
            subTarget = 0 - a
            while j < k:
                b = nums[j]
                c = nums[k]
                if result and result[-1][1] == b and result[-1][2] == c and result[-1][0] == a:
                    j += 1
                    k -= 1
                    continue
                sm = b + c
                if sm == subTarget:
                    result.append([a,b,c])
                    j += 1
                    k -= 1
                elif sm < subTarget:
                    j += 1
                else:
                    k -= 1
                
                
        print(result)
        return result
                    