#User function Template for python3

def downwardDigonal(n, matrix): 
    result = []
    
    for i in range(n):
        x, y = 0, i 
        while x < n and y >= 0:
            result.append(matrix[x][y])
            x += 1
            y -= 1
    
    for i in range(1, n):
        x, y = i, n-1
        while x < n and y >= 0:
            result.append(matrix[x][y])
            x += 1
            y -= 1
    
    return result
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends