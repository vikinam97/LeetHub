#User function Template for python3
from collections import defaultdict

class Solution:
    def maxGroupSize(self, arr, N, K):
        modMap = defaultdict(int)
        
        for i in range(len(arr)):
            modMap[arr[i]%K] += 1
        
        i, j = 1, K-1
        result = 0
        
        while i < j:
            result += max(modMap[i], modMap[j])
            i += 1
            j -= 1
        
        if modMap[0] > 0: result += 1
        if i == j and modMap[i] > 0: result += 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxGroupSize(arr,N,K))
# } Driver Code Ends