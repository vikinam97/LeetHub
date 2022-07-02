class HeapNode:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
    
    def __lt__(self, other):
        # max heap
        return self.freq > other.freq

class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        freq = {}
        
        for i in range(len(s)):
            if s[i] not in freq:
                node = HeapNode(s[i], 0)
                freq[s[i]] = node
                heap.append(node)
            freq[s[i]].freq += 1
        
        heapq.heapify(heap)
        result = []
        while heap:
            node = heapq.heappop(heap)
            result += [node.key] * node.freq
        
        return "".join(result)
            
            
            
        