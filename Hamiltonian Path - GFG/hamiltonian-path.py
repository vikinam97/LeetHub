#User function Template for python3

from collections import defaultdict

class Solution:
    
    
    def recur(self, node, edgeList, visited):
        
        if len(visited) == len(edgeList)-1:
            return True
            
        for v in edgeList[node]:
            if v in visited:
                continue
            visited.add(v)
            if self.recur(v, edgeList, visited):
                return True
            visited.remove(v)
    
    def check(self, N, M, Edges): 
        edgeList = [[] for _ in range(N+1)]
        
        for u, v in Edges:
            edgeList[u].append(v)
            edgeList[v].append(u)
        
        visited = set()
        for i in range(1, N+1):
            visited.add(i)
            if self.recur(i, edgeList, visited):
                return True
            visited.remove(i)
        
        return False
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends