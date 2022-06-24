#User function Template for python3

class Solution:
    def profession(self, level, pos):
        count = 0
        n = pos - 1
        
        while n != 0:
            n = n & n-1
            count += 1
        
        return 'd' if count & 1 else 'e'

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        level, pos = [int(x) for x in input().split()]
        
        ob = Solution()
        if(ob.profession(level, pos) == 'd'):
            print("Doctor")
        else:
            print("Engineer")
# } Driver Code Ends