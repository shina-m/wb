class Solution:
    
    def bs(self, A, i,j,t):
        
        m = (i+j)//2
        if A[m] == t:
            return m
        elif i == j or m < 0:
            return -1
        elif A[m] < t:
            return self.bs(A, m+1, j, t)
        else:
            return self.bs(A, i, m-1, t)
        
        
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) -1, target)