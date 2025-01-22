# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        level = 0
        res = [[]]
        q = deque([(root,0)])

        while q:
            curr,lvl = q.popleft()
            if lvl != level:
                res.append([])
                level+=1
            res[level].append(curr.val)

            if curr.left: q.append((curr.left,lvl+1))
            if curr.right: q.append((curr.right,lvl+1))
        
        return [x[-1] for x in res]