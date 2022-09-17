class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


class Solution1:
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