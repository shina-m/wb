class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        par_score = []
        total_score = 0
        
        for c in S:
            if c == '(':
                par_score.append(0)
                
            elif c == ')':
                val = max(par_score.pop(), 1)
                
                if len(par_score) > 0:
                    par_score[-1] += 2*val
                else:
                    total_score += max(val,1)
                    
        return total_score