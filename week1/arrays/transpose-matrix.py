class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = [[0]*len(A) for _ in A[0]]
        
        for i,row in enumerate(A):
            for j,cell in enumerate(row):
                B[j][i]= cell
        
        return B
                