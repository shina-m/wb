class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        import collections
        
        J = set(J)
        S = collections.Counter(S)
        
        result = 0
        
        for k,v in S.items():
            if k in J:
                result += v
                
        return result
                