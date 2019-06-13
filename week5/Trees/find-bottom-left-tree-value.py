# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.result = root.val
        self.max_depth = -1
    
        
        def depth(p, d):
            if not p: 
                return True
                    
            if depth(p.left, d+1):
                if d > self.max_depth:
                    self.max_depth = d
                    self.result = p.val
                
            if depth(p.right, d+1):
                if d > self.max_depth:
                    self.max_depth = d
                    self.result = p.val
            
        depth(root, 0)
        return self.result