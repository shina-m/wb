class Solution:
    
    
    def findSet(self, y, disjoint_set):
        
        for k,v in disjoint_set.items():
            if y in v:
                return k

    
    
    def mergeSet(self, disjoint_set, root_map, x_root, y_root):
        disjoint_set[x_root] = disjoint_set[x_root].union(disjoint_set[y_root])
        for y in disjoint_set[y_root]:
            root_map[y] = x_root
        
        del disjoint_set[y_root]
        
        return disjoint_set, root_map
            
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        root_map = {}
        disjoint_set = {}
        size = len(M)
        
        for x in range(size):
            root_map[x] = x
            disjoint_set[x] = set([x])
            


        for x in range(size):
            for y in range(x+1, size):

                if M[x][y]==1:
                    
                    x_root = root_map[x]
                    y_root = self.findSet(y, disjoint_set)
                    #x_root = self.findSet(x, disjoint_set)
                    #y_root = root_map[y]
                    
                    if x_root != y_root:
                        disjoint_set, root_map = self.mergeSet(disjoint_set, root_map, x_root, y_root)
                        
    
        return len(disjoint_set)
        

        