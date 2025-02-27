\\\
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
\\\

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        copy = {}
        copy[node.val] = Node(node.val, [])
        q = deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n.val not in copy: #the key is node.val not node
                    copy[n.val] = Node(n.val, [])
                    q.append(n)
                copy[curr.val].neighbors.append(copy[n.val])
            print(copy)
        return copy[node.val]