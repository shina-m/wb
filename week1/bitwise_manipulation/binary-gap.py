class Solution:
    def binaryGap(self, N: int) -> int:
        x = bin(N)[2:]
        
        start = -1
        max_dist = 0
        for i in range(len(x)):
            if x[i]=='1':
                if start != -1:
                    max_dist = max(max_dist, i-start)
                    start = i
                else:
                    start = i
            
                
        return max_dist