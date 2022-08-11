import heapq

class TreeNode:
    def __init__(self, val, freq, left=None, right=None):
        self.val = val
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    
    def dfs(self, node, path):
        # print(node)
        if node and not node.left and not node.right:
            self.codes.append("".join(path))
            return
        
        path.append('0')
        self.dfs(node.left, path)
        path.pop()
        path.append('1')
        self.dfs(node.right, path)
        path.pop()
    
    def huffmanCodes(self,S,f,N):
        heap = []
        for i in range(N):
            heap.append(TreeNode(S[i], f[i]))
        
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            
            node = TreeNode(a.val + b.val, a.freq + b.freq, a, b)
            
            heapq.heappush(heap, node)
        
        self.codes = []
        self.dfs(heap[0], [])
        
        return self.codes