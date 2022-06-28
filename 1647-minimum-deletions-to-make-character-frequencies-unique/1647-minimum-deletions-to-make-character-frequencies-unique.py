class Solution:
    def minDeletions(self, s: str) -> int:
        countHash = defaultdict(int)
        for char in s:
            countHash[char] += 1
        
        countingList = list(countHash.values())
        print(countingList)
        countingList.sort(reverse=True)

        deleteCount = 0
        seenFreq = {}
        for i in range(1,len(countingList)):
            # if countingList[i] >= countingList[i-1]:
            while countingList[i] > 0 and countingList[i] >= countingList[i-1]:
                countingList[i] -= 1
                deleteCount += 1
            print(countingList, countingList[i], countingList[i-1])
        
        return deleteCount
        
        