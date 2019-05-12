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
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            else:
                root = root.children[c]
            
        return root.terminates
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            else:
                root = root.children[c]
            
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)