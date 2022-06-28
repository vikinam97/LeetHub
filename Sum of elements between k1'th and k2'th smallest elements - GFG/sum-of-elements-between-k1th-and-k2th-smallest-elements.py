#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        temp = sorted(A)
        idxHash = {}
        for i in range(len(A)):
            idxHash[temp[i]] = i
        
        start = idxHash[temp[K1-1]]
        end = idxHash[temp[K2-1]]
        # print(temp, start, end)
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