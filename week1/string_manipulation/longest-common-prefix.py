class Solution:
    
    def get_prefix(self, i, strs):
        
            t = strs[0][i]
            for s in strs[1:]:
                if s[i] !=t:
                    return ''
            return t
                    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = []
        min_len = sys.maxsize
        for x in strs:
            min_len = min(min_len, len(x))
        
        if min_len == sys.maxsize:
            return ''.join(output)
        
        
        for i in range(min_len):
            t = self.get_prefix(i, strs)
            if  t =='':
                return ''.join(output)
            else:
                output.append(t)
            
        return ''.join(output)
        