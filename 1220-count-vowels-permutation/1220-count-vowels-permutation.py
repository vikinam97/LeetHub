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

    def countVowelPermutation(self, n: int) -> int:
        # Solution - DP iterative
        # Time - O(N*5)
        # Space - O(N*5)
        
        pdp = [1] * 5
            
        for i in range(1, n):
            cdp = [0] * 5
            for j in range(5):
                for ni in self.adj[j]:
                    cdp[j] = (cdp[j]  + pdp[ni] % self.MOD) % self.MOD
            pdp = cdp
            
        p = 0
        for val in pdp:
            p = (p + val % self.MOD) % self.MOD

        return p

class Solution1:
    
    MOD = (10 ** 9) + 7
    vowels = ['a', 'e', 'i', 'o', 'u']
    adj = {
        0: [1], 
        1: [0, 2], 
        2: [0, 1, 3, 4],
        3: [2, 4], 
        4: [0]
    }

    def countVowelPermutation(self, n: int) -> int:
        # Solution - DP iterative
        # Time - O(N*5)
        # Space - O(N*5)
        
        dp = [[0] * 5 for i in range(n)]
        for i in range(5):
            dp[0][i] = 1
            
        for i in range(1, n):
            for j in range(5):
                for ni in self.adj[j]:
                    dp[i][j] = dp[i][j] + dp[i-1][ni]
        
        p = 0
        for val in dp[-1]:
            p = (p + val % self.MOD) % self.MOD

        return p

class Solution1:
    
    MOD = (10 ** 9) + 7
    @cache
    def recur(self, cur, n):
        if n == 0:
            return 1
        
        p = 0
        for aj in ['a', 'e', 'i', 'o', 'u']:
            if (cur, aj) in self.adjList:
                p = (p + self.recur(aj, n-1) % self.MOD) % self.MOD
        
        return p
    
    def countVowelPermutation(self, n: int) -> int:
        # Solution - DP
        # Time - O(N*5)
        # Space - O(N*5)
        
        self.adjList = {(-1, 'a'): 1, (-1, 'e'): 1, (-1, 'i'): 1, (-1, 'o'): 1, (-1, 'u'): 1, ('a', 'e'): 1, ('e', 'a'): 1, ('e', 'i'): 1, ('i', 'a'): 1, ('i', 'e'): 1, ('i', 'o'): 1, ('i', 'u'): 1, ('o', 'i'): 1, ('o', 'u'): 1, ('u', 'a'): 1}
        
        return self.recur(-1, n)