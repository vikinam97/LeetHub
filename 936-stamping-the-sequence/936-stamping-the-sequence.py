class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """

        stamp = list(stamp)
        target = list(target)
        ns = len(stamp)
        nt = len(target)
        
        left = nt
        res = []
        flag = True # if nothing is changed during one loop, then finish the while loop
        while left > 0 and flag:
            flag = False
            for i in range(nt - ns + 1):
                if left == 0:
                    break
                    
                if all([target[i + j] == '?' for j in range(ns)]):
                    continue
                
                if all([stamp[j] == target[i + j] or target[i + j] == '?' for j in range(ns)]):
                    flag = True
                    res.insert(0, i)
                    for j in range(ns):
                        if stamp[j] == target[i + j]:
                            target[i + j] = '?'
                            left -= 1
    
        return res if left == 0 else []