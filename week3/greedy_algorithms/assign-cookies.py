class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        r = 0
        g.sort()
        s.sort()
        
        si, sl = 0, len(s)
        gi, gl = 0, len(g)
        
        while si != sl and gi != gl:
            match = False
            if g[gi] <= s[si]:
                r += 1
                gi += 1
                match = True
                
            si +=1
                    
        return r
                    
                    
            
        