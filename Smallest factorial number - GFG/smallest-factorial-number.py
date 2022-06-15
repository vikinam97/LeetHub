#User function Template for python3

class Solution:
    def countTrailZero(self, n):
        i = 5
        count = 0
        while i <= n:
            count += n // i
            i = i * 5
        return count
        
    def findNum(self, n : int):
        
        # low=0
        # high=n*5
        # ans=low
        # while(low<=high):
        #     mid=(low+high)//2
        #     zeros = self.countTrailZero(mid)
        #     if(zeros>=n):
        #         ans=mid
        #         high=mid-1
        #     else:
        #         low=mid+1

        # return ans
        
        l, r = 0, 5 * n
        ans = l
        while l <= r:
            
            mid = (l+ r) // 2
            
            trailZeroCount = self.countTrailZero(mid)
            
            if trailZeroCount >= n:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends