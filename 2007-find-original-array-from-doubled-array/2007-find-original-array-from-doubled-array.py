class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        queue, result = collections.deque([]), []
        
        changed.sort()
        for i in range(len(changed)):
            if queue and queue[0] == changed[i]:
                queue.popleft()
                continue
            
            queue.append(changed[i] * 2)
            result.append(changed[i])
            
        if queue: return []
        
        return result 
                
        
        
        

class Solution1:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Solution - Sorting + Map
        # Time - O(NlogN)
        # Space - O(N)
        
        t = len(changed) / 2
        if t != int(t):
            return []
        
        changed.sort()
        hashMap = defaultdict(list)
        for i in range(len(changed)):
            hashMap[changed[i]].append(i)
        
        result = []
        
        for i in range(len(changed)):
            if changed[i] == -1:
                continue
                
            if not len(hashMap[changed[i] * 2]):
                return []
            
            tar = hashMap[changed[i] * 2].pop()
            
            if tar < i:
                return []
            
            changed[tar] = -1            
            result.append(changed[i])
        
        return result
        