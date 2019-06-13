class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {0:set(), 1:set()}
                
        def dfs(v,uk,vk):
            if v in visited[uk]:
                return False
            elif v in visited[vk]:
                return True
            
            visited[vk].add(v)
            
            uk,vk = vk,uk
            for x in graph[v]:
                if dfs(x,uk,vk) == False:
                    return False
            
            return True
        
        for i in range(len(graph)):
            if i not in visited[0] and i not in visited[1]:
                if dfs(i, 0, 1) == False:
                    return False
                
        return True
                
                