#User function Template for python3

class Solution:
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        # Solution - using diff array
        # Time O(Q + N)
        # Space O(N) 

        diffList = [0] * length

        for i, j, val in updates:
            diffList[i] += val
            if j+1 < length:
                diffList[j+1] -= val

        for i in range(1, len(diffList)):
            diffList[i] = diffList[i] + diffList[i-1]

        return diffList