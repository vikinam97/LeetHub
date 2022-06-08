class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return "0"
        
        if(num < 0):
            num += pow(2, 32)
        result = []
        while num > 0:
            rem = num % 16
            num = num // 16
            if rem > 9:
                rem = chr(ord('f') - (15 - rem))
            result.append(rem)
        
        result.reverse()
        return "".join([str(a) for a in result])