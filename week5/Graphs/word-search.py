class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        
        def get_neighb_land(i,j):
            r = []
            for x,y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if -1 <x< rows and -1 <y< cols:
                    r.append((x,y))  
            return r
                        
                    
        def dfs(i,j, ci, visited):
            
            if ci == len(word):
                return True
            
            if (i,j) in visited or board[i][j] != word[ci]:
                return False
                   
            if ci+1 == len(word):
                return True
            
            visited.add( (i,j) )
            
            for x,y in get_neighb_land(i,j):
                if dfs(x, y, ci+1, visited.copy()) == True:
                    return True
            return False
        
                    
    
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j, 0, set()):
                    return True
            
        return False
                    
        