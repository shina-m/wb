class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = bin(n)[2:]
        
        if number[0] != '1':
            return False
        else:
            for x in number[1:]:
                if x != '0':
                    return False
                
        return True
        