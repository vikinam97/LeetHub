#User function Template for python3

class Solution:
    def posIntSol(self,s):
        n = len(s.split('+'))
        k = int(s.split('=')[1])
        
        if k <= n:
            return 0
        
        # using pascal triangle to calculate k-1 C n-1
        triangle = [[1]]
        for i in range(1, k):
            row = [0] * (i+1)
            triangle.append(row)
            row[0] = 1
            row[-1] = 1
            
            for j in range(1, i):
                # print(i, j)
                triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
        
        # print(triangle, k, n)
        return triangle[k-1][n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.posIntSol(s))
# } Driver Code Ends