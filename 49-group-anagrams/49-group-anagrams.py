class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpSet = defaultdict(list)
        
        for i in range(len(strs)):
            key = sorted(strs[i])
            key = "".join(key)
            grpSet[key].append(strs[i])
        
        return grpSet.values()
        
        