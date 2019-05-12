class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        ls = len(s)
        if ls != len(t):
            return False
        
        rs = {}
        visited_t = set()
        for i in range(ls):
            if (s[i] in rs and rs[s[i]] != t[i]) or (s[i] not in rs and t[i] in visited_t):
                #print(rs, s[i], t[i])
                return False
                
            rs[s[i]] = t[i]
            visited_t.add(t[i])
        return True
                