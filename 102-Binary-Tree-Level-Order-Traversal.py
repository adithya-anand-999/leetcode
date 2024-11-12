# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        prev_lvl = 0
        res = [[]]
        queue = deque([(root, 0)])
        #recursive traversal is for dfs, for bfs iterative is easier

        while queue:
            node,lvl = queue.popleft()
            if lvl != prev_lvl:
                res.append([])
                prev_lvl+=1
            res[lvl].append(node.val)
            if node.left: queue.append((node.left, lvl+1))
            if node.right: queue.append((node.right, lvl+1))
        return res
        
        