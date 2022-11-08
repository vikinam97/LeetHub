#User function Template for python3

from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        countMap = Counter(Arr)
        result = []
        
        for key in countMap:
            if countMap[key] & 1:
                result.append(key)
        
        if result[0] < result[1]:
            return [result[1], result[0]]
        
        return result
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends