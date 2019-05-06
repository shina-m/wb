class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:].zfill(32)
        y = bin(y)[2:].zfill(32)
        
        out = 0
        
        for i in range(32):
            if x[i] != y[i]:
                out += 1
                
        return out