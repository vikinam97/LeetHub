class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.s = s
        self.size = len(s)
        self.wl = len(words[0])
        span = len(words)*self.wl
        self.count = Counter(words)
        self.ans = []
        for i in range(min(self.wl, self.size-span+1)):
            self.match(i, i)
        return self.ans  

    def match(self, i, j):
        cur = deepcopy(self.count)
        while j + self.wl <= self.size:
            w = self.s[j:j+self.wl]
            if w in cur:
                cur[w] -= 1
                if cur[w] == 0:
                    del cur[w]
                if not cur:
                    self.ans += i,
                    cur[self.s[i:i+self.wl]] += 1
                    i += self.wl
                j += self.wl
            else:
                if i < j:
                    cur[self.s[i:i+self.wl]] += 1
                    i += self.wl
                else:
                    j += self.wl
                    i += self.wl