class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        temp = [ (abs(a-x), i, a) for i, a in enumerate(arr)]
        
        temp.sort()
        
        result = [ a for _, i, a in temp[:k]]
        result.sort()
        return result
        
        
        