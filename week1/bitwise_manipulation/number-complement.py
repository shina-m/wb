class Solution:
    def findComplement(self, num: int) -> int:
        x = list(bin(num)[2:])
        
        for i in range(len(x)):
            x[i] = '1' if x[i] == '0' else '0'
        
        return int(''.join(x),2)