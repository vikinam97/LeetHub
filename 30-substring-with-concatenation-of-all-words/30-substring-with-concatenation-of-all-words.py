class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, num_words = len(s), len(words)
        if n == 0 or num_words == 0:
            return []
        count = collections.Counter(words)
        word_len = len(words[0])
        total_len = num_words * word_len
        res = []
        i = 0
        while i <= n - total_len:
            # determine whether s[i:i+total_len] is valid
            seen = collections.defaultdict(int)
            for j in range(i, i + total_len, word_len):
                w = s[j:j + word_len]
                if w in count:
                    seen[w] += 1
                    if seen[w] > count[w]:
                        break
                else:
                    break    
            if seen == count:
                res.append(i)
            i = i + 1
        return res