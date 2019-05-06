class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = 0
        for i,x in enumerate(A):
            if x%2 == 0:
                A[i],A[j] = A[j],A[i]
                j += 1
            
        return A