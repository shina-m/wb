class Solution:
    
    def get_digit_squares(self, n):
        r = []
        for x in str(n):
            d_int = int(x)
            d_sqr = d_int*d_int
            r.append(d_sqr)
        
        return str(sum(r))
        
    
    def not_cycle(self,mem, n):
        sqr = self.get_digit_squares(n)
        #print(sqr, mem)
        if sqr == '1':
            return True
        elif sqr in mem:
            return False

        else:
            mem.add(sqr)
            n = sqr
            return self.not_cycle(mem, n)
            

       #iterative method 
#     def isHappy(self, n: int) -> bool:
#         t = str(n)
#         mem = set(t)
        
        
#         while True:
#             ds = self.get_digit_squares(t)
#             if ds == '1':
#                 return True
#             elif ds in mem:
#                 return False
#             else:
#                 t = ds
                
    
    # recursive method
    def isHappy(self, n: int) -> bool:
        t = [str(n)]
        mem = set(t)
        return self.not_cycle(mem,n)
        
        