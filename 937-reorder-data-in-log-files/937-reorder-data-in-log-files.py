class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digiLogs = []
        ltrLogs = []
        for log in logs:
            temp = log
            log = log.split(" ")
            if log[-1][0].isnumeric():
                digiLogs.append(temp)
            else:
                ltrLogs.append((" ".join(log[1:]), log[0]))
        
        result = []
        
        ltrLogs.sort()
        for log in ltrLogs:
            result.append(log[1] + " " +log[0])
        
        return result + digiLogs