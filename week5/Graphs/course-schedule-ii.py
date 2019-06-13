class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        seen = [0] * numCourses
        for x in prerequisites:
            edges[x[0]].append(x[1])

        result = []

           
        def recursive_helper(node):
            for neighbor in edges[node]:
                
                if seen[neighbor] == 0:
                    seen[neighbor] = -1
                    
                    if recursive_helper(neighbor) == False:
                        return False
                    
                    seen[neighbor] = 1
                    
                elif seen[neighbor] == -1:
                    return False
                
            if node not in result:
                result.append(node)

        for x in range(numCourses):
            if recursive_helper(x) == False:
                return []
        return result