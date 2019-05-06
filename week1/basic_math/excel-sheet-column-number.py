class Solution:
    def titleToNumber(self, s: str) -> int:
        start = ord('A') - 1 #64
        base = ord('Z') - start #26
        number = 0 
        s_len = len(s)
        
        for i in range(s_len-1,-1,-1):
            
            number += math.pow(base, s_len-i-1) * (ord(s[i]) - start)
            
        return int(number)
        