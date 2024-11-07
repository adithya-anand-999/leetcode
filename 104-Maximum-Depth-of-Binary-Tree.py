# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def help(node,lvl):
            if not node: return lvl
            left, right = help(node.left, lvl+1), help(node.right, lvl+1)
            return max(left,right)
        return help(root,0)

