# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #use the fact that the tree is a binary search tree, meaning child to the left of root is less than root, the child to right of root is more than root. 

        #Running into issue where I am returning None, even though it looks like I should be returning the node itself. 
        pV,qV = p.val,q.val

        def help(node):
            #No need for base case as we are gaurenteed to return a value 
            # if not node:
            #     return
            nV = node.val
            
            # if nV == pV or nV == qV or ((pV < nV and qV > nV) or (pV > nV and qV < nV)):
            #     return node
            if nV < pV and nV < qV:
                print(1)
                return help(node.right)
            elif nV > pV and nV  > qV:
                print(2)
                return help(node.left)
            else:
                print(3)
                return node
        return help(root)
