# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def help(node):
            if not node:
                return (True, 0)
            left, right = help(node.left), help(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            #is there a way to break out of all recrusion, and just clear the call stack. Once I see that balanced is false in any level of recursion. I can conclude that the entire tree is unbalanced, there would be no need for my to continue recusing. 
            return (balanced, 1+max(left[1], right[1]))
        return help(root)[0]

            # left2.left = (True, 2), left2.right = (True,1)
            # left2 = (True,3)
            # right2 = (True,1)
            # root.left = left2
            # root.right = right2
