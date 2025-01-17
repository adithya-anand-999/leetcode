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
            if not help(node.left, min, node.val) or not help(node.right, node.val, max):
                return False
            return True
        return help(root, float('-inf'), float('inf'))