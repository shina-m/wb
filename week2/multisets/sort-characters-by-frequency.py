class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        r = ''
        for k,v in counter.most_common():
            r += k*v
            
        return r