#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Solution - sorting and hashing
        # Time O(NlogN) sorting
        # Space O(N) hash map
        temp = sorted(A)
        idxHash = {}
        
        start = K1-1
        end = K2-1
        
        return sum(temp[start+1:end])
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends