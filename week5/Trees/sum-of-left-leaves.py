# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0
        
        def inorder(x, side):
            if x == None:
                return True

            l = inorder(x.left, 'l')
            r = inorder(x.right, 'r')
            
            if l and r and side == 'l':
                self.total += x.val
                
        inorder(root, 'r')
        return self.total

                
                
        