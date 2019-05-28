class Solution:
    import sys
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pl = len(points)
        if pl <= 0: return 0
        
        points.sort(key = lambda x:x[0])
        rg = [-sys.maxsize,sys.maxsize]
        r = 1
    
        for x in points:
            if rg[0] <= x[0] <= rg[1]:
                rg = [x[0], min(x[1],rg[1])]
                
            else:
                r += 1
                rg = [x[0], x[1]]
                
            
        return r