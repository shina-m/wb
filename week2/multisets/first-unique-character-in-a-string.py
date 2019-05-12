class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        s_count = Counter(s)
        for i,c in enumerate(s):
            if s_count[c] ==1:
                return i
            
        return -1
        