# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def help(node):
            if not node: return False
            if node == p or node == q: return node
            left,right = help(node.left),help(node.right)
            if left and right: return node
            return left or right
        return help(root)