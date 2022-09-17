wordDict = { word:i for i, word in enumerate(words) }
result = []
for i, word in enumerate(words):
# word itself reversed exists
rev = word[::-1]
if rev in wordDict and wordDict[rev] != i:
result.append([i, wordDict[rev]])
# prefix of palindromic sub string or sub string exists
for prefix in self.getPrefix(word):
revP = prefix[::-1]
if revP in wordDict:
result.append([i, wordDict[revP]])
# siffix of plaindromic sub string or rev sub string exists
for suffix in self.getSuffix(word):
revS = suffix[::-1]
if revS in wordDict:
result.append([wordDict[revS], i])
return result
```