class Solution:
    
    def bfs(self, varA, varB, graph):
        childs = [(varA, 1)]
        seenSet = {}
        
        while childs:
            nxt = []
            
            for edge in childs:
                var, val = edge
                if var == varB:
                    return val
                
                if var in seenSet:
                    continue
                seenSet[var] = 1
                
                for nVar, nVal in graph[var]:
                    
                    nxt.append((nVar, nVal * val))
            
            childs = nxt
            
        return -1
        
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
        varSet = set()
        
        for i in range(len(equations)):
            varA, varB = equations[i] 
            val = values[i]
            
            varSet.add(varA)
            varSet.add(varB)
            
            if varA not in graph:
                graph[varA] = []
            graph[varA].append((varB, val))
            
            if varB not in graph:
                graph[varB] = []
            graph[varB].append((varA, 1 / val))
        
        
        result = []
        for i in range(len(queries)):
            varA, varB = queries[i]
            
            if varA not in varSet or varB not in varSet:
                result.append(-1)
                continue
                
            result.append(self.bfs(varA, varB, graph))
        
        return result
            
            