class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        d_sorted = []
        for i,x in enumerate(S):
            if x not in d:
                d[x] = [i,i,1]
                d_sorted.append(x)
            else:
                d[x][1] = i
                d[x][2] += 1
                
        rnge = [-1, 1]
        r = 0
        r_len = [0]
        
        for x in d_sorted:
            if rnge[0] < d[x][0] < rnge[1]:
                rnge[1] = max(d[x][1], rnge[1]) 
                r_len[r] += d[x][2]
                
            else:
                r +=1
                rnge = d[x][:2] 
                r_len.append(d[x][2])
                
        return r_len