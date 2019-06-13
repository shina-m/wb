# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Copied
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int: 
        self.result = 0

        def recursive(x):
            if x == None: 
                return 0

            l = recursive(x.left)
            r = recursive(x.right)

            self.result = max(self.result, l+r)

            return 1 + max(l,r)

        recursive(root)
        return self.result