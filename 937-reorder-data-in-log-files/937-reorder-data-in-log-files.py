class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Solution - parsing + sorting
        # Time - (NlogN + N + M)
        #     - N = len(ltrLogs)
        #     - M = len(digiLogs)
        # Space - O(N+M)
        
        digiLogs = []
        ltrLogs = []
        for log in logs:
            temp = log
            log = log.split(" ", maxsplit=1)
            if log[-1][0].isnumeric():
                digiLogs.append(temp)
            else:
                ltrLogs.append((log[1], log[0]))
        
        result = []
        
        ltrLogs.sort()
        for log in ltrLogs:
            result.append(log[1] + " " +log[0])
        
        return result + digiLogs