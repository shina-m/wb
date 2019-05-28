class Solution:
    def bs(self, A, i,j,t):
        
        if j-i <= 3:
            for ix in range(i, j+1):
                if t <= A[ix]:
                    return ix
            return j+1
        
        m = (i+j)//2
        
        if t == A[m]:
            return m
        elif t > A[m]:
            return self.bs(A, m+1, j, t)
        else:
            return self.bs(A, i, m-1, t)
        
    
    def binary_insertion (self, lst, n):
        i = self.bs(lst, 0, len(lst)-1, n)
        return lst[:i]+ [n] + lst[i:] 
    
    
    def binary_deletion (self, lst, n):
        i = self.bs(lst, 0, len(lst)-1, n)
        del lst[i]
        return lst

    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_sub = sorted(p)
        s_sub = sorted(s[0: len(p)-1])
        r = []
        
        lp = len(p)-1
        
        for i in range(lp, len(s)):
            start = i-lp
            s_sub = self.binary_insertion(s_sub, s[i])
            
            if s_sub == p_sub:
                r.append(start)
            
            s_sub = self.binary_deletion(s_sub, s[start])
                
        return r
        