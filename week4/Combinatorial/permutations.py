class Solution:
    def recurse (self,A, r):
        if A == []:
            self.result.append(r)
            return
        else:
            for i in range(len(A)):
                x = r + [A[i]]
                self.recurse(A[:i] + A[i+1:], x)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recurse(nums, [])
        
        return self.result