class Solution:
    def isPalindrome(self, s: str) -> bool:

        i,j = 0, len(s)-1
        
        while i<=j:
            
            if not s[i].isalnum() :
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
                
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i,j = i+1, j-1
            
        return True
        