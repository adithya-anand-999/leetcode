# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def help(node, min, max):
            if not node: return True
            if min >= node.val or node.val >= max: return False
            left,right = help(node.left, min, node.val), help(node.right, node.val, max)
            if not left or not right: return False
            return True
        return help(root, -float('inf'), float('inf'))
        