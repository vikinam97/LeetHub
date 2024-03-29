from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution - Topo Sort
        # Time - O(N*P)
        # Space - O(N*P)
        
        
        links = defaultdict(list)
        courseDep = [0] * numCourses
        for a, b in prerequisites:
            links[b].append(a)
            courseDep[a] += 1
        
        bfs = []
        
        for i in range(len(courseDep)):
            if courseDep[i] == 0:
                bfs.append(i)
        seen = set()
        
        while bfs:
            nxt = []

            for c in bfs:
                seen.add(c)
                for nei in links[c]:
                    if nei in seen:
                        continue
                    
                    if courseDep[nei] > 0:
                        courseDep[nei] -= 1
                    if courseDep[nei] == 0:
                        nxt.append(nei)
                    
            bfs = nxt
        
        for i in range(len(courseDep)):
            if courseDep[i] != 0:
                return False
        
        return True
                        
        
        
        
        
            
        