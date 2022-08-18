class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Solution - Greedy - choosing max freq element first
        # Time - O(NlogN)
        # Space - (N)
        
        freqSet = defaultdict(int)
        heap = []
        for num in arr:
            freqSet[num] += 1
        
        for num in freqSet:
            heap.append(-1 * freqSet[num])
        
        heapq.heapify(heap)
        
        count, size = 0, 0
        
        while heap and size < (len(arr) // 2):
            size += -1 * heapq.heappop(heap)
            count += 1
        
        return count
        
        
            
            