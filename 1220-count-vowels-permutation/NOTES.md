```
class Solution:
MOD = (10 ** 9) + 7
vowels = ['a', 'e', 'i', 'o', 'u']
adj = {
0: [1],
1: [0, 2],
2: [0, 1, 3, 4],
3: [2, 4],
4: [0]
}
​
def countVowelPermutation(self, n: int) -> int:
# Solution - DP iterative + space optimized
# Time - O(N*5)
# Space - O(1)
pdp = [1] * 5
for i in range(1, n):
cdp = [0] * 5
for j in range(5):
for ni in self.adj[j]:
cdp[j] = (cdp[j] + pdp[ni] % self.MOD) % self.MOD
pdp = cdp