class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        mid_length = (len(s)-1)/2
        i,j = int(math.floor(mid_length)), int(math.ceil(mid_length))

        while i >= 0:
            s[i],s[j] = s[j],s[i]
            i,j = i-1,j+1
