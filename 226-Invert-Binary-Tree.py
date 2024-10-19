# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        for each node its left child flips with its right child. No need to flip if the node 
        does not have children. If the node has no children we just return, if the node has 1
        child then we just move the child from left to right or right to left. For such checks
        of children we have to make sure the node itself exists, I think that check alone will
        suffice for children cases. 
        '''

        def help(node):
            #this will have unnessesary recursion for each leaf node, we can stop this by having cases for all 3 possibilites of 1 child, 2 child, or 0 child. Extra code but some level of better runtime. 
            if not node:
                return 
            node.left, node.right = node.right, node.left
            help(node.left)
            help(node.right)
            #in the inbetween states of recursion the return node will return the node but its value is of no use, it might be computatially inefficent. 
            # return node

#how can I be sure that this function will actually modify the children of the root, so it does modify the tree of the argument passed and not make a copy with root and modify that tree and not the original tree. 
        help(root)
        return root
        
        