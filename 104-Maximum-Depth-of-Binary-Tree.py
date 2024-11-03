# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def help(node,level):
            nonlocal res

            if not node:
                return 
            left,right = help(node.left,level+1),help(node.right,level+1)
            res = max(res, level)
        help(root,1)
        return res