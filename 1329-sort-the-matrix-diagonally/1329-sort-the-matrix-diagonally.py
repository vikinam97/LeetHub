class Solution:
    def diagonalSort(self, A):
        # Solution - get vales, sort and put back
        # Time - O(NlogN)
        # Space - O(1)
        
        n, m = len(A), len(A[0])
        hashMap = defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                hashMap[i - j].append(A[i][j])
                
        for key in hashMap:
            hashMap[key].sort(reverse=True)
            
        for i in range(n):
            for j in range(m):
                A[i][j] = hashMap[i - j].pop()
                
        return A
        