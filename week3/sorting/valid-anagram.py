class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        
        if ls != lt: return False
        
        return sorted(t) == sorted(s) 
        