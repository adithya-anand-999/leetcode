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
        copy[node] = Node(node.val, [])
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in copy:
                    copy[n] = Node(n.val, [])
                    queue.append(n)
                copy[curr].neighbors.append(copy[n])
        return copy[node]
