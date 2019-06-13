class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        self.total = 0
        
        
        def get_neighb_land(i,j):
            r = []
            for x,y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if -1 <x< rows and -1 <y< cols and grid[x][y] == 1:
                    r.append([x,y])      
            return r
                        
                    
        def dfs(i,j):
            if (i,j) in visited:
                return
            self.total +=4
            visited.add((i,j))
            for x,y in get_neighb_land(i,j):
                self.total -= 1
                dfs(x,y)  
                    
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.total
                    
        
        
        
            
                
     
        
                    
                
        