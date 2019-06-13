"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    #recursive
#     def postorder(self, root: 'Node') -> List[int]:
#         self.result = []
        
#         def helper(x):
#             if x == None:
#                 return []
            
#             for c in x.children:
#                 helper(c)
        
#             self.result.append(x.val)
            
#         helper(root)
        

#         return self.result

    #iterative
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root == None: return result
        res = []
        stack = [root]
        while stack:
            r = stack.pop()

            if r == None: continue
            res.append(r.val)
            stack.extend(r.children)

        return res[::-1]
