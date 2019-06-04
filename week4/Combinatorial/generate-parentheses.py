#based on recommended resources
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ['('] * n + [')'] * n
        
        res = [''.join(s)]
        
        while True:
            o, c = 0, 0  
            for i in range(1, 2 * n + 1):

                if i == 2 * n:
                    return res

                if s[-i] == '(':
                    o += 1
                    if c > o:
                        s[-i:] = [')'] + ['('] * o + [')'] * (c - 1)
                        break
                else:
                    c += 1

            res.append(''.join(s))