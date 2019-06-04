class Solution:
    def recurse (self,A, k, r):
        if k == 0:
            self.result.append(r)
            return
        else:
            for i in range(len(A)):
                x = r+[A[i]]
                self.recurse(A[i+1:], k-1, x)
                
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        if n == 0:
            return ['']
        
        self.recurse(list(range(1, n+1)), k, [] )
        
        return self.result
        