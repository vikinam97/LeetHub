```
class Solution:
def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
# Solution - binary search to partition list
# Time O(log(min(A, B)))
# Space O(1)
totalSize = len(A) + len(B)
half = totalSize // 2
# ensuring the A is smaller
if len(B) < len(A):
A, B = B, A
l, r = 0, len(A) - 1
while True:
i = (l + r) // 2
j = half - (i+1) - 1
Aleft = A[i] if i >= 0 else float('-infinity')
Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
Bleft = B[j] if j >= 0 else float('-infinity')
Bright = B[j + 1] if (j+1) < len(B) else float('infinity')
if Aleft <= Bright and Bleft <= Aright:
if totalSize % 2 == 0:
return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
else:
return min(Aright, Bright)
elif Aleft > Bright:
r = i - 1
else:
l = i + 1
```
​