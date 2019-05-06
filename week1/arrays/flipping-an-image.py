class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i,x in enumerate(A[:]):
            y = []
            for j in range(len(x)-1, -1, -1):
                t = 1 if x[j]== 0 else 0
                y.append(t)
            
            A[i] = y
            
        return A
        