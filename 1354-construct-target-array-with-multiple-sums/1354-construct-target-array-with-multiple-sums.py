class Solution:
	def isPossible(self, target: List[int]) -> bool:

		heapq._heapify_max(target)
		s = sum(target)

		while target[0] != 1:
			sub = s - target[0]
			if sub == 0: return False
			n = max((target[0] - 1) // sub, 1)
			s -= n * sub
			target0 = target[0] - n * sub
			if target0 < 1: return False
			heapq._heapreplace_max(target, target0)

		return True

# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#         minHeap = []
        
#         if len(target) == 1:
#             if target[0] == 1:
#                 return True
#             else:
#                 return False
        
#         for i in range(len(target)):
#             heapq.heappush(minHeap, target[i])
            
#         curSum = len(target)
#         while len(minHeap) != 0:
#             curTarget = heapq.heappop(minHeap)
            
#             if curTarget == 1:
#                 continue
                
#             check = (curTarget - 1) % (curSum - 1)
#             if check != 0 and check != len(target):
#                 return False
#             curSum += curTarget - 1
        
#         return True