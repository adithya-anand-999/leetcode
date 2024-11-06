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
        visited = {}
        visited[node] = Node(node.val, [])
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in visited:
                    #n has not been seen before, so we need to make its copy 
                    visited[n] = Node(n.val, [])
                    #we have also not seen n's neighbors before
                    queue.append(n)
                visited[curr].neighbors.append(visited[n])
        return visited[node]