#User function Template for python3

class Solution:
    def minPartition(self, N):
        denoms = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        val = N
        i = 0
        result = []
        while val > 0:
            
            while denoms[i] > val:
                i += 1
            
            count = val // denoms[i]
            val -= count*denoms[i]
            
            result += [denoms[i]] * count
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends