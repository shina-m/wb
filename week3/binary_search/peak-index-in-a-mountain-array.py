class Solution:
    def bs(self, A,i,j):
        m = (i+j) //2
        if (m == i or A[m-1] <= A[m])  and (j == m or A[m] > A[m+1]):
            return m
        
        elif i == j == m:
            return -1
        
        elif (m != i and A[m-1] < A[m]):
            return self.bs(A, m+1, j)
        
        else:
            return self.bs(A, i, m)
        
        
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        c = {}
        for i,x in enumerate(A):
            c[i] = x
        
        return sorted(c, key = c.get)[-1]
        #return self.bs(A, 0, len(A)-1)

        