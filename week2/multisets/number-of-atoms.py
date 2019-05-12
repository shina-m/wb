class Solution:
    
    def get_trailing_digit(self, i):
        start = i
        while i+1 < self.lf and self.f[i+1].isdigit() != False:
            i+=1
        
        if start == i:
            return 1, start
        else:
            return int(self.f[start+1:i+1]), i
                
            
    def countOfAtoms(self, formula: str) -> str:
        c = collections.Counter()
        self.f = formula
        self.lf = len(self.f)
        brackets = 0
        bracket_contents = []
        
        i = 0
        while i < self.lf:
            if self.f[i] == '(':
                bracket_contents.append( collections.Counter() )
                brackets +=1
                
                
            elif self.f[i].isupper():
                name = self.f[i]
                
                if i+1 < self.lf and self.f[i+1].islower():
                    name += self.f[i+1]
                    i +=1
                
                val,i = self.get_trailing_digit(i)
                
                if brackets != 0:
                    bracket_contents[-1][name] += val
                else:
                    c[name] += val
                
                
            elif self.f[i] == ')':
                mult,i  = self.get_trailing_digit(i)
                for k,v in bracket_contents[-1].items():
                    bracket_contents[-1][k] = mult * v

                brackets -=1
                
                if brackets != 0:
                    bracket_contents[-2] =  bracket_contents[-2] +  bracket_contents[-1]
                    
                else:
                    c  = c + bracket_contents[-1]

                del bracket_contents[-1]
                   
            i +=1
              
        r = ''
        for k,v in sorted(c.items(), key=lambda x:x[0]):
            r +=k
            if v !=1:
                r+=str(v)
        
        return r
        