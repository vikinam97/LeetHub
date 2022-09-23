class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        total = len(A) + len(B)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A
            
        l, r = 0, len(A) -1
        
        while True:
            
            i = l + ((r - l) // 2)
            j = half - (i+1) - 1
            
            aLeft = A[i] if i >= 0 else float('-inf')
            aRight = A[i+1] if i+1 < len(A) else float('inf')
            bLeft = B[j] if j >= 0 else float('-inf')
            bRight = B[j+1] if j+1 < len(B) else float('inf')
            
            if aLeft <= bRight and bLeft <= aRight:
                if total & 1:
                    return min(aRight, bRight)
                else:
                    return (min(aRight, bRight) + max(bLeft, aLeft)) / 2
            
            if aLeft < bRight:
                l = i + 1
            else:
                r = i - 1
            
            
        
            