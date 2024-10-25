# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def help(node) -> Tuple[bool,int]:
            if not node:
                return (True, 0)
            left, right = help(node.left), help(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

#the issue is in the part 1 + max(left[0], right[0]), the 0th index are the bool values, you know they should be the height values. Silly mistake. 
            return (balanced, 1 + max(left[1], right[1]))
        return help(root)[0]