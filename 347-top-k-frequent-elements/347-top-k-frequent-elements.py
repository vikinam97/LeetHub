class HeapNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        # for max heap comparison operator
        return self.val > other.val
        
class Solution:
    # Solution - Heap
    # Time - O(N) 
    #     - heapify takes O(N) time only
    # Space - O(N)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = defaultdict(int)
        
        for i in range(len(nums)):
            if nums[i] not in freq:
                node = HeapNode(nums[i], 1)
                freq[nums[i]] = node
                heap.append(node)
            
            freq[nums[i]].val += 1
        
        heapq.heapify(heap)
        
        result = []
        while heap and len(result) < k:
            result.append(heapq.heappop(heap).key)
        
        return result
        
        
            