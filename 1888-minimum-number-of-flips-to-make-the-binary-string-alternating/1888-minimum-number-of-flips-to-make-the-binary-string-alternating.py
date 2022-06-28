class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        diff1,diff2 = 0,0
        alt1,alt2 = "",""
        s=s+s
        alt1, alt2 = "01" * n, "10" * n
        l=0
        res = len(s)
        for r in range(len(s)):
            if s[r]!=alt1[r]:
                diff1+=1
            if s[r]!=alt2[r]:
                diff2+=1
            if r>=n:
                if n%2!=0: 
                    if s[l]!=alt1[l]:
                        diff1-=1
                    if s[l]!=alt2[l]:
                        diff2-=1
                l+=1
            if r >= n-1:
                res = min(res,diff1,diff2)
        return res

# class Solution:
#     def minFlips(self, s: str) -> int:
#         strStarting1 = []
#         strStarting0 = []
#         string = s + s
        
#         # for starting 1 string
#         curChar = '1'
#         for i in range(len(s)):
#             if curChar == s[i]:
#                 strStarting1.append(0)
#             else:
#                 strStarting1.append(1)
#             curChar = '0' if curChar == '1' else '1'
        
#         # starting 0 string
#         curChar = '0'
#         for i in range(len(s)):
#             if curChar == s[i]:
#                 strStarting0.append(0)
#             else:
#                 strStarting0.append(1)
#             curChar = '0' if curChar == '1' else '1'
        
#         minStarting1 = 0
#         minStarting0 = 0
#         for i in range(int(len(strStarting1) / 2)):
#             minStarting1 += strStarting1[i]
#             minStarting0 += strStarting0[i]
        
#         sliding1 = minStarting1
#         sliding0 = minStarting0
#         j = 0
#         for i in range(int(len(strStarting1) / 2), len(strStarting1)):
#             sliding1 += strStarting1[i]
#             sliding1 -= strStarting1[j]
            
#             sliding0 += strStarting0[i]
#             sliding0 -= strStarting0[j]
            
#             minStarting1 = min(minStarting1, sliding1)
#             minStarting0 = min(minStarting0, sliding0)
            
#         return min(minStarting1, minStarting0)
        