# Time - O(N * M)
# - worst case .... traverse all chars
return self.dfs(0, word, self.trie)
def dfs(self, i, word, trie):
if i >= len(word):
return self.end in trie
if word[i] == '.':
for key in trie:
if key == self.end:
continue
if self.dfs(i + 1, word, trie[key]):
return True
elif word[i] in trie:
return self.dfs(i + 1, word, trie[word[i]])
return False
​
​
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```