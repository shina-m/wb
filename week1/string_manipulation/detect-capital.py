class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].islower() and word.islower():
            return True
            
        elif word[0].isupper():
            if word.isupper() or word[1:].islower():
                return True
            
        return False