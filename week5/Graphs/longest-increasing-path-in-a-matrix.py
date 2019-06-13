class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if matrix == []:
            return 0
            
        result = 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        
        def get_neighb(i,j):
            r = []
            for x,y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if -1 <x< rows and -1 <y< cols and matrix[x][y] > matrix[i][j]:
                    r.append((x,y))  
            return r

        def recursive_helper(i,j, ln):
            l = ln
            
            for i,j in get_neighb(i,j):
               
                if (i,j) in memo:
                    l = max(l, memo[(i,j)])
                else:
                    memo[(i,j)] = recursive_helper(i,j, ln)
                    l = max(l, memo[(i,j)])
                
            return l+1

        for i in range(rows):
            for j in range(cols):
                ln = 0
                result = max(recursive_helper(i,j, ln), result)
                
        return result
