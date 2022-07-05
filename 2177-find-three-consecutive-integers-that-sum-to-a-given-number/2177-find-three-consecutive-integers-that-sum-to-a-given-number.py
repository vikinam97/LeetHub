class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        
        if ((3 * x)) == num:
            return [(x-1), x, (x+1)]
        
        return []