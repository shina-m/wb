class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminates = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.get_node()
        
        
    def get_node(self):
        return TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = self.get_node()
                
            root = root.children[c]
            
        root.terminates = True
        
    
    def starts_with_terminates(self, word: str, cursor = None) -> bool:
        """
        Returns if the word is in the trie.
        """

        root = cursor if cursor else self.root
        
        for c in word:
            if c not in root.children:
                return False, False
            else:
                root = root.children[c]
            
        return root, root.terminates
    
        

class Solution:
    
    def get_neighbors(self,i,j):
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        n = []
        for a,b in directions:
            if 0 <= i+a < self.nrows and 0 <= j+b < self.ncols:
                n.append((i+a, j+b))
        return n
    
    
    def recurse(self, i,j, w, visited, cursor):
        w += self.b[i][j]
        
        starts_with, terminates = self.t.starts_with_terminates(w[-1], cursor)

        if terminates:
            self.result.add(w)

        if starts_with:
            visited.add((i,j))
            nbs = self.get_neighbors(i,j)
            for x in nbs:
                if x not in visited:
                    self.recurse(x[0],x[1], w, visited.copy(), starts_with)

         
    def get_words(self, i, j):
        visited = set()
        starts_with = True
        w =''
        self.recurse(i,j,w, visited, None)
        
        
 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if len(board) == 0:
            return
        
        self.b = board
        self.nrows = len(board)
        self.ncols = len(board[0])
        
        self.t = Trie()
        for w in words:
            self.t.insert(w)
            
        self.result = set()
        
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.get_words(i,j)
                
        return list(self.result)