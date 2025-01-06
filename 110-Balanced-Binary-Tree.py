# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def help(node,height):
            if not node: return (True, 0)
            left,right = help(node.left,height), help(node.right,height)
            valid = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            height = max(left[1], right[1]) + 1
            return (valid,height)
        return help(root,0)[0]

