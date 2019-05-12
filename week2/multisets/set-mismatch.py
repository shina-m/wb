class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        expected = Counter(range(1, len(nums)+1))
        values = Counter(nums)
        
        r = [None, None]
    
        for k,v in expected.items():
            if values[k] != v:
                if values[k] == 2:
                    r[0] = k
                else:
                    r[1] = k
                    
            if None not in r:
                return r
                    