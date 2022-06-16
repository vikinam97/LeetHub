class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Solution - using two pointer and 3Sum
        # Time -> O(n^3) 
        # Space -> O(1)
        
        L = len(nums)
        ans = []
        if L<4:
            return ans
        nums.sort()

        for i in range(L-3):
            a = nums[i]
            if ans and a == ans[-1][0]:
                continue
            for j in range(i+1, L-2):
                b = nums[j]
                if ans and a == ans[-1][0] and b ==ans[-1][1]:
                    continue
                start = j+1
                end = L-1
                sub_target = target-a-b
                while start<end:
                    if nums[start]+nums[end] == sub_target:
                        if ans and b==ans[-1][1] and nums[start] == ans[-1][2] and nums[end]==ans[-1][-1]:
                            start+=1
                            end-=1      
                            continue
                        ans.append([a,b,nums[start], nums[end]])
                        start+=1
                        end-=1
                    elif nums[start]+nums[end] > sub_target:
                        end-=1
                    else:
                        start+=1
        return ans
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         Solution - hash map 
#         Time - O(N^2) worse O(N^3)
#         Space - O(N^2)
#         sumDict = defaultdict(list)
        
#         resultHash = {}
#         resultList = []
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 sm = nums[i] + nums[j];
#                 if (target - sm) in sumDict:
#                     for pairs in sumDict[target - sm]:
#                         temp = pairs[:]
#                         temp.append(nums[i])
#                         temp.append(nums[j])
#                         resultList.append(temp)
#             for j in range(i):
#                 sm = nums[i] + nums[j]
#                 sumDict[sm].append([nums[i], nums[j]])
        
#         return resultList
                
        