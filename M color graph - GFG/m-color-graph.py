def graphColoring(graph, k, V):
    # Solution - back tracking - chossing all ossible color path for node
    # Time - O(M*V)
    #     - M = no of colors
    #     - V = no of nodes
    # Space - O(V)
    
    colors = [-1] * V
    return recur(0, graph, k, V, colors)
    
def recur(i, graph, k, V, colors):
    if i == V:
        return True
    
    for c in range(k):
        
        canUse = True
        
        for adj, val in enumerate(graph[i]):
            if val == 1 and colors[adj] == c:
                canUse = False
                break
            
        if not canUse:
            continue
        
        colors[i] = c
        if recur(i + 1, graph, k, V, colors):
            return True
        colors[i] = -1
    
    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends