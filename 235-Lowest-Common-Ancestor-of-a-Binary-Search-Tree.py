# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        p_val, q_val = p.val, q.val

        while queue:
            curr = queue.popleft()
            curr_val = curr.val
            # if (curr_val >= p_val and curr_val <= q_val) or curr_val == q_val or curr_val == p_val: return curr

            if curr_val > p_val and curr_val > q_val: queue.append(curr.left)
            elif curr_val < p_val and curr_val < q_val: queue.append(curr.right)
            else: return curr