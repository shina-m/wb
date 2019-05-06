class Solution:
    
    def find(self,x):
        if self.parent[x] !=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
    def union(self, x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot]> self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[xroot] = yroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[yroot] += 1
                
        self.root[x] = xroot
        self.root[y] = yroot
                
        
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        m = len(board)
        n = len(board[0])
        
        self.parent = {}
        self.root = {}
        self.rank = {}
        self.border_os = []
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    self.parent[(i,j)] = (i,j)
                    self.rank[(i,j)] = 0
                    
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        self.border_os.append((i,j))
                        
                        
                    
        for i,j in self.rank.keys():
            if i+1<m and j<n and board[i+1][j]=='O':
                self.union((i,j), (i+1,j))
            if i<m and j+1<n and board[i][j+1]=='O':
                self.union((i,j), (i,j+1))
                
        self.border_roots = set()
        for i,j in self.border_os:
            r = self.root[(i,j)] if (i,j) in self.root else self.find((i,j))
            self.border_roots.add(r)
            
        #get list of roots that do not have a border element
        for k in self.parent.keys():
            r = self.root[k] if k in self.root else self.find(k)
            if r not in self.border_roots:
                board[k[0]][k[1]] = 'X' 