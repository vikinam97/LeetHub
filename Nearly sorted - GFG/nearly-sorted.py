#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        # Solution - using min heap
        # Time - O(NlogK)
        # Space - O(K)
        heap = []
        for i in range(k):
            heapq.heappush(heap, a[i])
        
        for i in range(k, n):
            heapq.heappush(heap, a[i])
            idx = i - k
            a[idx] = heapq.heappop(heap)

        i = n-k
        while len(heap) != 0:
            a[i] = heapq.heappop(heap)
            i += 1
        
        return a
        
        
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends