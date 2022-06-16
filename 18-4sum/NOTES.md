start+=1
return ans
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         Solution - hash map
#         Time - O(N^2) worse O(N^3)
#         Space - O(N^2)
#         sumDict = defaultdict(list)
#         resultHash = {}
#         resultList = []
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 sm = nums[i] + nums[j];
#                 if (target - sm) in sumDict:
#                     for pairs in sumDict[target - sm]:
#                         temp = pairs[:]
#                         temp.append(nums[i])
#                         temp.append(nums[j])
#                         resultList.append(temp)
#             for j in range(i):
#                 sm = nums[i] + nums[j]
#                 sumDict[sm].append([nums[i], nums[j]])
#         return resultList