class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #if we think of greedy approach as ultimatly all the odd indices will have same value
        #and all the even indices will have the same value that is not same as the odd value
        if len(nums) == 1:
            return 0
        oddMap = {}
        evenMap = {}
        oddMap[-1] = 0
        evenMap[-1] = 0
        for i in range(0,len(nums),2):
            if nums[i] in oddMap:
                oddMap[nums[i]] += 1
            else:
                oddMap[nums[i]] = 1
        for i in range(1,len(nums),2):
            if nums[i] in evenMap:
                evenMap[nums[i]] += 1
            else:
                evenMap[nums[i]] = 1
        maxOdd = -1
        maxOdd2 = -1
        for i in oddMap:
            if maxOdd == -1:
                maxOdd = i
            elif maxOdd2 == -1:
                maxOdd2 = i
            if oddMap[maxOdd] < oddMap[i]:
                maxOdd2 = maxOdd
                maxOdd = i
            else:
                if maxOdd2 != -1 and oddMap[maxOdd2] <= oddMap[i]:
                    maxOdd2 = i
        maxEven = -1
        maxEven2 = -1
        for i in evenMap:
            if maxEven == -1:
                maxEven = i
            elif maxEven2 == -1:
                maxEven2 = i
            if evenMap[maxEven] < evenMap[i]:
                maxEven2 = maxEven
                maxEven = i
            else:
                if maxEven2 != -1 and evenMap[maxEven2] <= evenMap[i]:
                    maxEven2 = i
        if maxEven != maxOdd:
            return len(nums) - evenMap[maxEven] - oddMap[maxOdd]
        else:
            return min(len(nums)-evenMap[maxEven]-oddMap[maxOdd2],len(nums)-evenMap[maxEven2]-oddMap[maxOdd])