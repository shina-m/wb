class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ti, tl = 0, len(t)
        r = len(s)
        
        for x in s:
            while ti < tl:
                ti += 1
                if x == t[ti-1]:
                    r-=1
                    break
                    
        return r == 0