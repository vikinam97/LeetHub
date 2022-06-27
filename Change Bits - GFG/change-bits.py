#User function Template for python3

class Solution:
    def changeBits(self, N):
        Nprime = 0
        temp, i = N, 0
        while temp != 0:
            Nprime = Nprime | 1 << i
            temp = temp >> 1
            i += 1
        
        return [Nprime - N, Nprime]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans = ob.changeBits(N)
        
        print(ans[0],ans[1])
# } Driver Code Ends