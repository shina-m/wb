class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals, key = lambda x:x[0])
        rg = [intervals[0][0],intervals[0][1]]
        res = []
        
        for x in intervals[1:]:
            if x[0] <= rg[1]:
                rg[1] = max(rg[1],x[1])
            else:
                res.append(rg)
                rg = x
                
        if res == [] or res[-1] != rg:
            res.append(rg)
            
        return res