class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countSetBits(n):
            count = 0
            while n != 0:
                count += 1
                n = n & (n-1)
            
            return count
        
        resultList = []
        for i in range(n+1):
            temp = countSetBits(i)
            resultList.append(temp)
            
        return resultList;
            