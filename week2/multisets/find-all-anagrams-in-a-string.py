'''
I got this algo. on my own, but it was timing out because instead of increasing/decreasing an element in the counter, I was creating a counter in each iteration which
made my algo. timeout.
'''
class Solution:
    
    def equal_counters(self, a,b):
        for i,k in a.items():
            if b[i] != k:
                return False
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter

        lp = len(p)
        p_count = Counter(p)
        s_count = Counter(s[0:lp-1])
        r = []
        for i in range(lp-1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                r.append(i-(lp-1))
            
            s_count[s[i-(lp-1)]] -= 1
            
            if s_count[s[i-(lp-1)]] == 0:
                del s_count[s[i-(lp-1)]]  
                
        return r