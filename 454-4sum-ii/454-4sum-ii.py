class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Soltion - hash table
        # Time - O(N^2)
        # Space - O(N^2)
        dictSum = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                dictSum[num2 + num1] += 1
        
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sm = num3 + num4
                if (0 - sm) in dictSum:
                    count += dictSum[0-sm]
        
        return count
        