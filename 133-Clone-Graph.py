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
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.append(n)
                visited[curr].neighbors.append(visited[n])
        return visited[node]

        # first = True
        # head = None

        # while queue:
        #     curr = queue.pop()
        #     currNode = Node(curr.val, curr.neighbors)
        #     if first:
        #         head = currNode
        #         first = False
        #     visited.append(curr.val)
        #     for n in curr.neighbors:
        #         if n not in visited:
        #             queue.append(n)
        # return head
