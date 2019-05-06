class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        carry = 0
        
        for i in range(len(digits)-1, -1,-1):
            digits[i] += carry
            carry = digits[i]//10
            
            if carry ==0:
                break
            
            else:
                digits[i] = digits[i]%10
                
        
        if carry > 0:
            digits = [carry]+digits
            
        return digits
        