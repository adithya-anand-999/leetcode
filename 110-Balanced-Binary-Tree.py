# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def help(node):
        #     if not node:
        #         return 0
        #     left = 1 + help(node.left)
        #     right = 1 + help(node.right)

        #     if abs(left-right) > 1:
        #         return False
        #     return True
        # return help(root)


        #You need to return 2 values at a time, saying if that node is balanced and returning a value of the height. 

        def dfs(node):
            if not node:
                return [True, 0]
            left,right = dfs(node.left),dfs(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]