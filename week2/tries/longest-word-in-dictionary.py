class TrieNode:
    def __init__(self): 
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, word):
        root = self.root

        for i,c in enumerate(word):
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]

        root.end_of_word = True


    def search_with_term_count(self, word):
        root = self.root
        for i,c in enumerate(word):
            if c not in root.children or not root.children[c].end_of_word:
                return False
            root = root.children[c]

        return root.end_of_word


class Solution:
    
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x : len(x), reverse=True)
        t = Trie()
        for w in words:
            t.insert(w)
            
        r = []
        for w in words:
            if t.search_with_term_count(w) and (len(r) ==0 or len(r[-1]) == len(w)):
                r.append(w)
        
        if r != []:
            return sorted(r)[0]
        else:
            return ''
            
            