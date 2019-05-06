class Solution:
    
    
    def find(self,x):      
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]

    def union(self, x, y):
        
        x_root = self.find(x)
        y_root = self.find(y)
    
        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] = self.rank[y_root] + 1

        
        self.groups -=1

            
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        
        self.rank = {}
        self.parent = {}
        irows = len(grid)
        icols = len(grid[0])
        
        self.groups = 0
        for i in range(irows):
            for j in range(icols):
                if grid[i][j]== '1':
                    self.parent[(i,j)] = (i,j)
                    self.rank[(i,j)] = 0
                    self.groups +=1
                
                
        for i,j in self.rank.keys():
            
            if (i+1<irows and j<icols and grid[i+1][j]=='1'):
                self.union((i,j), (i+1,j))
                
                
            if (i<irows and j+1<icols and grid[i][j+1]=='1'):
                self.union((i,j), (i,j+1))
               
        #print (self.parent)         
        return self.groups 
                
        