class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        edges = collections.defaultdict(list)
        tym = {}
        vtym = [6001] * (N+1)
        visited = set()
        self.result = 0
        
        for x in times:
            edges[x[0]].append(x[1])
            tym[(x[0], x[1])] = x[2]

            
        q =  [K]
        vtym[K] = 0
        
        while q != []:
            u = q.pop(0)
            visited.add(u)
            
            for v in edges[u]:
                if v not in q:
                    vtym[v] = min(vtym[v],  vtym[u]+tym[(u,v)])
                    q.append(v)

        return max(vtym[1:]) if  max(vtym[1:]) != 6001 else -1