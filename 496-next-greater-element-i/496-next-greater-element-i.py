class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet = {}
        for i in range(len(nums1)):
            hashSet[nums1[i]] = i
        
        resultList = [-1] * len(nums1)
        # decreasing order
        monoStack = []
        for i in range(len(nums2)):
            while monoStack and monoStack[-1] < nums2[i]:
                ele = monoStack.pop()
                if ele in hashSet:
                    resultList[hashSet[ele]] = nums2[i]
            
            monoStack.append(nums2[i])
        
        return resultList
                