# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True
        