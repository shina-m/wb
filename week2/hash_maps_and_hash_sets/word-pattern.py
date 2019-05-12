class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        from collections import defaultdict
        ps = len(pattern)
        st = str.split(' ')
        
        if ps != len(st):
            return False
        
        rs = {}
        visited_st = set()
        
        for i in range(ps):
            if (pattern[i] in rs and rs[pattern[i]] != st[i]) or (pattern[i] not in rs and st[i] in visited_st):
                return False
                
            rs[pattern[i]] = st[i]
            visited_st.add(st[i])
            
        return True