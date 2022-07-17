class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        memo = [0 for i in range(k+1)]
        memo[0] = 1
        for i in range(2,n+1):
            tmp = [0 for i in range(k+1)]
            tmp[0] = 1
            for j in range(1,k+1):
                tmp[j] = tmp[j-1] + memo[j] - (memo[j-i] if j-i>=0 else 0)
            memo = tmp
        return memo[k] % (10**9+7)

# class Solution:
#     def recur(self,n , noOfEle, seenMap, k, prevMax):
#         if k < 0:
#             return 0
        
#         if noOfEle == 0:
#             print(seenMap, k)
#             return 1 if k == 0 else 0
        
#         count = 0
#         for num in range(1, n+1):
#             if num in seenMap:
#                 continue
                
#             self.array[noOfEle] = num
#             seenMap[num] = True
#             count += self.recur(
#                 n,
#                 noOfEle-1, 
#                 seenMap, 
#                 (k - 1 if prevMax > num else k),
#                 max(prevMax, num))
#             del seenMap[num]
        
#         return count
    
    
#     def kInversePairs(self, n: int, k: int) -> int:
        
#         self.array = [-1] * (n+1)
#         count = self.recur(n, n, {}, k, float('-inf'))
#         return count % ((10 ** 9) + 7)
        