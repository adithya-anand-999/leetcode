# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #for every level of the tree get the rightmost node
        #so output == levels of the tree. 
        # root is always included 

        if not root: return []
        res = [[]]
        level = 0
        q = deque([(root,0)])

        while q:
            curr,curr_level = q.popleft()
            if curr_level != level: 
                res.append([])
                level+=1
            res[level].append(curr.val)
            if curr.left: q.append((curr.left, curr_level+1))
            if curr.right: q.append((curr.right, curr_level+1))
        return [x[-1] for x in res]