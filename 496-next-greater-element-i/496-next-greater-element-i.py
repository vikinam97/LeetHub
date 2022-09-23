class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hashMap = {}
        
        nxtGrt = [-1] * len(nums2)
        
        for i in range(len(nums2)):
            hashMap[nums2[i]] = i
            while stack and nums2[i] > stack[-1][0]:
                val, idx = stack.pop()
                nxtGrt[idx] = nums2[i]
            
            stack.append([nums2[i], i])
        
        
        result = []
        for i in range(len(nums1)):
            idx = hashMap[nums1[i]]
            result.append(nxtGrt[idx])
        
        return result
            
        
        