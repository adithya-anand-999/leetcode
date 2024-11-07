# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        prev = 0
        queue = deque([(root,0)])
        res = [[]]

        while queue:
            node,lvl = queue.popleft()
            if lvl != prev:
                res.append([])
                prev = lvl
            # print(node.val,lvl)
            res[prev].append(node.val)

            if node.left:queue.append((node.left, lvl+1))
            if node.right:queue.append((node.right, lvl+1))
        return res

