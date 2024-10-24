# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def help(node):
            if p.val > node.val and q.val > node.val:
                return help(node.right)
            elif p.val < node.val and q.val < node.val:
                return help(node.left)
            else:
                return node
        return help(root)