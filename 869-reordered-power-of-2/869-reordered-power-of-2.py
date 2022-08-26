class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a = str(n)

        pList = list(permutations(a))
        for p in pList:
            if p[0] != '0' and bin(int("".join(p))).count('1') == 1:
                return True
            
        return False