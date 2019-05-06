class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        i,j = 0, len(s)-1
        s = list(s)
        
        while i<=j:
            if s[i].lower() not in vowels:
                i += 1
                continue
            elif s[j].lower() not in vowels:
                j-=1
                continue
            else:
                s[i],s[j] = s[j], s[i]
                i,j = i+1, j-1
                
        return ''.join(s)
            
        