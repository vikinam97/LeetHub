class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = {}
        maxSoFar = float('-inf')
        seenPath = []
        
        for i in range(len(edges)):
            if i in visited:
                continue
            seenPath = []
            
            cur, dist = i, 0
            while cur != -1:
                if cur in visited and visited[cur] == 'C':
                    break
                    
                if cur in visited:
                    maxSoFar = max(maxSoFar, dist - visited[cur])
                    break
                
                seenPath.append(cur)
                visited[cur] = dist
                dist += 1
                cur = edges[cur]
                
            for n in seenPath:
                visited[n] = 'C'
                
        return maxSoFar if maxSoFar != float('-inf') else -1