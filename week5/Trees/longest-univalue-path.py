# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def recursive(x):
            if x == None: 
                return 0

            l = recursive(x.left)
            r = recursive(x.right)
            
            if l and r and x.left.val == x.right.val == x.val:
                self.result = max(self.result, l+r+1)
                return 1 + max(l+r)
            
            if l and x.val == l.left.val:
                self.result = max(self.result, 1+l)
                return 1 + max(l+r)
                
            if l and x.val == l.right.val:
                self.result = max(self.result, 1+r)
                return 1 + max(l+r)
            
            return 0
                
            

        recursive(root)
        return self.result
        