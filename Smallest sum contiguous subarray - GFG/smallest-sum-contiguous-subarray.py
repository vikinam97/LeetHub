#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        minSoFar = A[0], 0, 0
        slidingSum = A[0]
        j = 0
        for i in range(1, len(A)):
            slidingSum = min(A[i], slidingSum+A[i])
            minSoFar = min(minSoFar, slidingSum)
            
            
        return minSoFar
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends