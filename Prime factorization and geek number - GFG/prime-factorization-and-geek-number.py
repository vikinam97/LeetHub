#User function Template for python3

class Solution:
    def geekNumber(self, N):
        i = 2
        while i * i <= N:
            count = 0
            while N % i == 0:
                count += 1
                N = N / i
            if count > 1:
                return 0
            i += 1
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        if ob.geekNumber(N)==1 :
            print("Yes");
        else :
            print("No");
# } Driver Code Ends