class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = collections.Counter(A.split())
        B = collections.Counter(B.split())
        
        r = []
        
        for k,v in A.items():
            if k in B:
                del B[k]
            elif v==1:
                r.append(k)
        
        for k,v in B.items():
            if (v==1) and (k not in A):
                r.append(k)
                
        return r
                