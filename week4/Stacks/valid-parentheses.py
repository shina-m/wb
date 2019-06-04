class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        par = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for c in s:
            if c in par.values():
                stack.append(c)
            elif c in par.keys():
                if stack == [] or stack.pop() != par[c]:
                    return False
         
        return True and stack == []
            
        