class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Solution - Hash Map on cntnt
        # Time - O(N*M)
        #     - N = len(rootPaths)
        #     - M = len(every folder files)
        # Space - O(N*M)
        
        
        cntntHash = defaultdict(list)
        
        for i in range(len(paths)):
            path = paths[i].split(" ")
            root = path[0]
            
            for file in path[1:]:
                tempFile = file.split("(")
                name, cntnt = tempFile[0], tempFile[1][:-1]
                
                cntntHash[cntnt].append(root + '/' + name)
        
        result = []
        for key in cntntHash:
            if len(cntntHash[key]) > 1:
                result.append(cntntHash[key])
        
        return result