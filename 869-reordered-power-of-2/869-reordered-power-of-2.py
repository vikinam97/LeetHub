class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for p in list(permutations(str(n))):
            if p[0] != '0' and bin(int("".join(p))).count('1') == 1:
                return True
            
        return False