# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def inorder(root, leaf):
            if root == None: return leaf
            
            if root.left == root.right == None:
                leaf.append(root.val)
                
            else:
                inorder(root.left, leaf)
                inorder(root.right, leaf)
                
            return leaf
        
        leaf1 = []
        leaf2 = []
        
        return inorder(root1, leaf1) == inorder(root2, leaf2)
            
            
        