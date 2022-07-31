class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # Solution - greedy sort and pick from sorted array
        # Time - O(N)
        # Space - O(1)
        
        grades.sort()
        
        curSum, curTotal = 0, 0
        lSum, lTotal = 0, 0
        count = 0
        i = 0
        
        for i in range(len(grades)):
            curSum += grades[i]
            curTotal += 1
            
            if curSum > lSum and curTotal > lTotal:
                count += 1
                lSum, lTotal = curSum, curTotal
                curSum, curTotal = 0, 0
        
        return count
            
        