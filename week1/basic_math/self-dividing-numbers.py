class Solution:
    def is_self_dividing(self, x):
        
        num = []
        for i in str(x):
            if i == '0':
                return False
            else:
                num.append(int(i))
        
        for j in num:
            if x%j != 0:
                return False
        
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for x in range(left, right+1):
        
            if self.is_self_dividing(x):
                output.append(x)
        
        
        return output