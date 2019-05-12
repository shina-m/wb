"""
Note: After trying for close to an hour, I made some progress on understanding the question lol, and also a logic to the solutions (kind of) but I still was stuck. so in frustration, I gave up on this and looked up a solution online that made logical sense.
"""
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        from collections import Counter
        r = set()
        for x in A:
            even = ''.join(sorted(x[0::2]))
            odd = ''.join(sorted(x[1::2]))

            r.add((even+odd))
        
        return len(r)