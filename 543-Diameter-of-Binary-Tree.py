# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def help(node):
            nonlocal maxLen

            if not node: return 0
            left,right = help(node.left), help(node.right)

            maxLen = max(maxLen, left+right)
            return 1+max(left,right)
        help(root)
        return maxLen